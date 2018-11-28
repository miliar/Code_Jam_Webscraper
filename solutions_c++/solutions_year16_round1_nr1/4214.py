#include <iostream>
#include <deque>

using namespace std;

using Seq = deque<char>;

char find_other(const Seq& seq)
{
    char result = seq[0];
    for (auto it = seq.begin(); it != seq.end(); ++it) {
        if (result != *it) {
            return *it;
        }
    }
    return seq[0];
}

Seq process(const string& s)
{
    Seq result;
    for (auto c : s) {
        if (result.size() == 0) {
            result.push_back(c);
        } else if (c > result[0]) {
            result.push_front(c);
        } else if (c < result[0]) {
            result.push_back(c);
        } else {
            char other = find_other(result);
            if (c > other) {
                result.push_front(c);
            } else {
                result.push_back(c);
            }
        }
    }
    return result;
}

int main()
{
    int test_cases;
    cin >> test_cases;

    for (int i = 0; i < test_cases; ++i)
    {
        string s;
        cin >> s;
        Seq result = process(s);
        cout << "Case #" << i + 1 << ": ";
        for (auto c : result) {
            cout << c;
        }
        cout << endl;
    }

    return 0;
}
