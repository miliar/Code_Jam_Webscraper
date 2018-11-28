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

bool ismatch(string strs[], vector<int> &ct, int n)
{
    bool match = true;
    for (int k = 0; k < strs[n].length(); k++)
    {
        if (ct[strs[n][k]-'A'] <= 0)
        {
            match = false;
            break;
        }
    }

    return match;
}

void flag(string strs[], vector<int> &ct, int n)
{
    for (int k = 0; k < strs[n].length(); k++)
    {
        if (ct[strs[n][k]-'A'] > 0)
            ct[strs[n][k]-'A']--;
    }
}

int main(void)
{
    //freopen("E:\\CodeJam\\A\\x64\\Debug\\A-small-attempt0.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
	//ios::sync_with_stdio(false);

    int t = 0;
    std::cin >> t;

    string strs[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    
    FOR(i,t)
    {
        string str;
        cin >> str;

        vector<int> ct(26);
        for (int j = 0; j < str.length(); j++)
        {
            ct[str[j]-'A']++;
        }

        int n = 0;
        std::stringstream ss;
        while (n < 10)
        {
            switch (n)
            {
            case 0:
            case 2:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
                if (ismatch(strs, ct, n))
                {
                    flag(strs, ct, n);
                    ss << n;
                }
                else
                    n++;
                break;
            case 1:
                if (ismatch(strs, ct, n))
                {
                    if (ct['W'-'A'] + ct['U'-'A'] > ct['O'-'A']-1)
                        n++;
                    else
                    {
                        flag(strs, ct, n);
                        ss << n;
                    }
                }
                else
                    n++;
                break;
            case 3:
                if (ismatch(strs, ct, n))
                {
                    if (ct['U'-'A'] > ct['R'-'A']-1)
                        n++;
                    else
                    {
                        flag(strs, ct, n);
                        ss << n;
                    }
                }
                else
                    n++;
                break;
            default:
                break;
            }
        }

        std::cout << "Case #" << i+1 << ": " << ss.str() << std::endl;

        FOR(x,26)
        {
            if (ct[x] > 0)
                std::cout << "Error Case #" << i+1 << ": " << char('A' + x) << ct[x]  << std::endl;
        }
    }

	return 0;
}

