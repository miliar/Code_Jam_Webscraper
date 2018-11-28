#include <iostream>
#include <stdio.h>
#include <string>
#include <set>

using namespace std;

int isVowel(char c)
{
    if((c == 'a')||(c == 'e')||(c == 'i')||(c == 'o')||(c == 'u')) return 1;
    else return 0;
}

int solve(const string &s, const int &n)
{
    set<pair<int,int>> parts;
    //cout << "input " << s << " " << n << endl;
    for(int i = 0; i <= (int)s.length() - n; ++i)
    {
        int isVowelInPart = 0;
        for(int j = i; j < i + n; ++j)
        {
            if(isVowel(s[j]))
            {
                isVowelInPart = 1;
                break;
            }
            //else cout << s[j] << " is not vowel" << endl;
        }
        if(!isVowelInPart)
        {
            //cout << "processing " << i << endl;
            for(int j = 0; j <= i; ++j)
            {
                for(int k = i+n-1; k < (int)s.length(); ++k)
                {
                    pair<int, int> p;
                    p.first = j;
                    p.second = k;
                    parts.insert(p);
                    //cout << "inserted " << j << "  " << k << endl;
                }
            }
        }
    }
    return parts.size();
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;

    for(int i = 1; i <= t; ++i)
    {
        string s;
        cin >> s;
        int n;
        cin >> n;
        cout << "Case #" << i << ": " << solve(s, n) << endl;
    }

    return 0;
}

