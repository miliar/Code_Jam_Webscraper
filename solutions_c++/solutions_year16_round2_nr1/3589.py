#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int remain[26];
vector<int> answer;

string numbers[10] = { 
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" 
};

bool f(int start)
{
    int sum = 0;
    for (int i = 0; i < 26; ++i)
        sum += remain[i];
    if (sum == 0)
        return true;

    for (int i = start; i < 10; ++i)
    {
        bool flag = true;
        for (int j = 0; j < numbers[i].size(); ++j)
        {
            if (remain[numbers[i][j] - 'A'] == 0)
            {
                flag = false;
                break;
            }
        }

        if (flag)
        {
            for (int j = 0; j < numbers[i].size(); ++j)
            {
                remain[numbers[i][j] - 'A']--;
            }

            answer.push_back(i);

            if (f(i))
                return true;

            answer.pop_back();
            
            for (int j = 0; j < numbers[i].size(); ++j)
            {
                remain[numbers[i][j] - 'A']++;
            }
        }
    }

    return false;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int T;

    in >> T;

    for (int t = 1; t <= T; ++t)
    {
        string s;
        in >> s;

        answer.clear();

        for (int i = 0; i < 26; ++i)
        {
            remain[i] = 0;
        }

        for (int i = 0; i < s.size(); ++i)
        {
            remain[s[i] - 'A']++;
        }

        if (!f(0))
            out << "impossible";

        out << "Case #" << t << ": ";
        for (int i = 0; i < answer.size(); ++i)
        {
            out << answer[i];
        }
        out << endl;
    }

    return 0;
}