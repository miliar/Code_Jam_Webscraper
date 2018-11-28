#include <string.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

map<string, int> ids;

int next_id = 1;

int word_id(string word)
{
    int id = ids[word];
    if(id)
        return id;
    else
    {
        ids[word] = next_id++;
        return ids[word];
    }
}

vector<int> words()
{
    vector<int> res;
    string str;
    assert(getline(cin, str));
    //cerr << "[" << str << "]\n";
    int ind = 0;
    for(int i = 0; i < str.size(); ++i)
        if(str[i] == ' ')
        {
            res.push_back(word_id(str.substr(ind, i - ind)));
            ind = i + 1;
        }
    res.push_back(word_id(str.substr(ind)));
    return res;
}

const int EE = 1, FF = 2;

void mark_sentence(vector<int> &flags, const vector<int> &sentence, int lang)
{
    for(int i = 0; i < sentence.size(); ++i)
        flags[sentence[i]] |= lang;
}

void solve(const int t)
{
    int N;
    string str;
    vector<vector<int> > sentences;
    assert(cin >> N);
    assert(getline(cin, str));
    for(int i = 0; i < N; ++i)
        sentences.push_back(words());
    vector<int> flags;
    
    int res = 1000000000;
    
    flags.resize(next_id + 10);
    
    for(int i = 0; i < 1 << (N - 2); ++i)
    {
        for(int i = 0; i < flags.size(); ++i)
            flags[i] = 0;
        mark_sentence(flags, sentences[0], EE);
        mark_sentence(flags, sentences[1], FF);
        for(int j = 0; j < N - 2; ++j)
            mark_sentence(flags, sentences[j + 2], (i & (1 << j)) ? EE : FF);
        int tmp = 0;
        for(int j = 0; j < flags.size(); ++j)
            if(flags[j] == (EE | FF))
                ++tmp;
        res = min(res, tmp);
    }
    cout << "Case #" << t << ": " << res << "\n";
}

int main()
{
    int T;
    
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        cerr << "Solving #" << t << "\n";
        solve(t);
    }
    return 0;
}
