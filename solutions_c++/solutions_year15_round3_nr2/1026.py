#include "cmath"
#include "iostream"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "functional"
#include "cstdio"

using namespace std;
typedef long long i64;

int entry_count(const string& a, const string& b)
{
    int t = 0;
    for (size_t from = 0; from < a.size(); ++from) {
        if (a.find(b, from) == from)
            ++t;
    }
    return t;
}

template <class F>
void generate(const string& alpha, size_t at, string& word, F func)
{
    if (at == word.size()) {
        func(word);
        return;
    }
    for (size_t i = 0; i < alpha.size(); ++i) {
        word[at] = alpha[i];
        generate(alpha, at + 1, word, func);
    }
}

double expected(int S, const string& kb, const string& w)
{
    if (S < int(w.size()))
        return 0.0;

    vector<int> freq(26);
    string alpha;

    for (auto c : kb) {
        ++freq[c - 'A'];
        if (freq[c - 'A'] == 1)
            alpha.push_back(c);
    }

    for (auto c : w)
        if (freq[c - 'A'] == 0)
            return 0.0;

    vector<double> prob(26);
    for (int i = 0; i < 26; ++i)
        prob[i] = double(freq[i]) / double(kb.size());

    int max_bananas = 0;
    double exp = 0.0;

    string probe(size_t(S), 0);
    generate(alpha, 0, probe, [&](const string& entry) {
        double p = 1;
        for (auto c : entry) {
            p *= prob[c - 'A'];
        }
        int x = entry_count(entry, w);
        max_bananas = max(max_bananas, x);
        exp += x * p;
    });

    return double(max_bananas) - exp;
}

int main()
{
    int T, K, L, S;
    cin >> T;
    string keyboard, word;
    for (int Ti = 1; Ti <= T; ++Ti) {
        cin >> K >> L >> S >> keyboard >> word;
        auto exp = expected(S, keyboard, word);
        printf("Case #%d: %.7f\n", Ti, exp);
    }
    return 0;
}
