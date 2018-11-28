#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <climits>
#include <stdio.h>
#include <cmath>
#include <set>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <fstream>
#include <unordered_map>
using namespace std;

#define INF INT_MAX / 2
#define OFFSET 11
#define NUM_ROWS 8
#define NUM_COLS 8
#define MAXN 1000 + OFFSET
#define MAXS 2500 + OFFSET
#define PRIMESCOUNT 143
#define MOD 1000000007

bool is_final(const string& s)
{
    for(int i = 0; i < s.size(); ++i)
    {
        if(s[i] != '+')
            return false;
    }
    return true;
}

string generate_string(string s, int n)
{
    string new_s = s;
    int q = n / 2;

    for(int j = 0; j < q; ++j)
    {
        char temp = new_s[j];
        new_s[j] = new_s[n-j-1];
        new_s[n-j-1] = temp;
    }
    for(int i = 0; i < n; ++i)
    {
        if(new_s[i] == '+')
        {
           new_s[i] = '-';
        } else if (new_s[i] == '-') {
           new_s[i] = '+';
        }
    }
    return new_s;
}

int main()
{
    unsigned long long in, t;
    string s;

    ifstream input("B-small-attempt0.in");
    ofstream output("B-small-attempt0.out");

    input >> t;
    //cin >> t;
    for (unsigned long long i = 1; i <= t; ++i)
    {
        input >> s;
        //cin >> s;
        queue<pair<string, unsigned long long> > q;
        unordered_map<string, bool> is_visited;

        q.push(make_pair(s, 0));

        while(!q.empty())
        {
            pair<string, unsigned long long> top = q.front();
            q.pop();

            is_visited.insert(make_pair(top.first, true));

            if(is_final(top.first))
            {
                output << "Case #" << i << ": " << top.second << endl;
                //cout << "Case #" << i << ": " << top.second << endl;
                break;
            }

            for (int i = top.first.size(); i >= 1; --i)
            {
                string new_s = generate_string(top.first, i);
                if(is_visited.find(new_s) == is_visited.end())
                    q.push(make_pair(new_s, top.second+1));
            }
        }
    }
    output.close();
    input.close();
    return 0;
}
