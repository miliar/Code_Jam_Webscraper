// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

#include "bigInt.h"
// BigInt::Rossi n1 ("314159265358979323846264338327950288419716939937510", BigInt::DEC_DIGIT);
// int stoi (const string& str, size_t* idx = 0, int base = 10);
// string to_string (val);

using namespace std;

#define FOR(i,n) for (int (i) = 0; (i) < (n); i++)
#define unsigned __int64 ulint
#define __int64 lint

vector<int> resort(vector<int> &s, vector<int> &si)
{
    vector<int> res;

    for (int i = 0; i < si.size(); i++)
    {
        int j = 0;
        for (; j < res.size(); j++)
        {
            if (s[si[i]] >= s[res[j]])
                break;
        }

        res.insert(res.begin()+j, si[i]);
    }

    return res;
}

int main(void)
{
    //freopen("E:\\CodeJam\\A\\x64\\Debug\\in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	//ios::sync_with_stdio(false);

    int t = 0;
    std::cin >> t;
    
    FOR(i,t)
    {
        int n = 0;
        cin >> n;
        vector<int> s;
        vector<int> si;
        int total = 0;
        int idx = 0;
        FOR(j,n)
        {
            int t = 0;
            cin >> t;
            s.push_back(t);
            total += t;

            int k = 0;
            for (; k < idx; k++)
            {
                if (s[idx] >= s[si[k]])
                    break;
            }
            si.insert(si.begin()+k, idx);

            idx++;
        }

        std::cout << "Case #" << i+1 << ":";

        while (total > 0)
        {
            cout << " ";
            if ((s[si[0]]-1)*2 <= (total-2) && (s.size()<3 || (s[si[2]])*2 <= (total-2)))
            {
                cout << char('A' + si[0]) << char('A' + si[1]);
                total -= 2;
                s[si[0]]--;
                s[si[1]]--;
            }
            else if (s[si[1]]*2 <= (total-2))
            {
                cout << char('A' + si[0]) << char('A' + si[0]);
                total -= 2;
                s[si[0]]--;
                s[si[0]]--;
            }
            else if (s[si[1]]*2 <= (total-1))
            {
                cout << char('A' + si[0]);
                total--;
                s[si[0]]--;
            }
            else
            {
                cout << "bad";
                break;
            }

            si = resort(s, si);
        }

        std::cout << std::endl;
    }

	return 0;
}

