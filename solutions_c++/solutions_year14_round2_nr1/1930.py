#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

string getLetters(string word)
{
    char prev = '_';
    string letters;
    for (auto c : word)
    {
        if (c != prev)
        {
            letters += c;
        }
        prev = c;
    }
    return letters;
}

void getCount(string word, vector<int>& countVec)
{
    int count = 1;
    char prev = '_';
    assert(countVec.empty());
    for (auto c : word)
    {
        if (c == prev)
        {
            count++;
        }
        else if (prev != '_')
        {
            countVec.push_back(count);
            count = 1;
        }
        prev = c;
    }
    countVec.push_back(count);
}

void solve()
{
    int N;
    cin >> N;

    string words[100];
    vector<int> counts[100];

    for (int i = 0; i < N; i++)
    {
        cin >> words[i];
    }

    string letters = getLetters(words[0]);

    for (int i = 1; i < N; i++)
    {
        if (getLetters(words[i]) != letters)
        {
            cout << "Fegla Won" << endl;
            return;
        }
    }

    for (int i = 0; i < N; i++)
    {
        getCount(words[i], counts[i]);
        assert(counts[i].size() == letters.size());
    }
    
    long result = 0;
    for (size_t i = 0; i < letters.size(); i++)
    {
        long avg = 0;
        for (int j = 0; j < N; j++)
        {
            avg += counts[j][i];
        }
        avg /= N;
        for (int j = 0; j < N; j++)
        {
            result += abs(counts[j][i] - avg);
        }
    }
    cout << result << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

