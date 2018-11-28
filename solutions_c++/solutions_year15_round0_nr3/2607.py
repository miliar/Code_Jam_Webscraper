#include<iostream>
#include<fstream>
#include<vector>
#include <string>
#include <stdio.h>
using namespace std;
ifstream fin("in.in");
ofstream fout("out.out");
#define cin fin
#define cout fout
bool isnegative(const char *s)
{
    return s[0] == '-';
}

char myabs(const char *s)
{
    if (isnegative(s))
        return s[1];
    return s[0];
}

string &mul(const char *s1, const char *s2, string &out)
{
    bool revers = isnegative(s1) != isnegative(s2);
    bool newneg = false;
    char result = myabs(s1);
    if (myabs(s2) != '1')
    {
        if (myabs(s1) == '1')
            result = myabs(s2), newneg = false;
        else if (myabs(s1) == myabs(s2))
            result = '1', newneg = true;
        else if (myabs(s1) == 'i' && myabs(s2) == 'j')
            result = 'k', newneg = false;
        else if (myabs(s1) == 'j' && myabs(s2) == 'k')
            result = 'i', newneg = false;
        else if (myabs(s1) == 'k' && myabs(s2) == 'i')
            result = 'j', newneg = false;
        else if (myabs(s1) == 'j' && myabs(s2) == 'i')
            result = 'k', newneg = true;
        else if (myabs(s1) == 'k' && myabs(s2) == 'j')
            result = 'i', newneg = true;
        else if (myabs(s1) == 'i' && myabs(s2) == 'k')
            result = 'j', newneg = true;
    }
    newneg ^= revers;
    out = "";
    if (newneg) out += '-';
    out += result;
    return out;
}

int main(void)
{
    int t;
    cin >> t;
    for (int x = 1; x <= t; x++)
    {
        int L, X, success = 0;
        string sum = "1";
        vector<string> vec;
        cin >> L >> X;
        for (int i = 0; i < L; i++)
        {
                char s; cin >> s;
                string ss; ss += s;
                vec.push_back(ss);
        }
        for (int i = 0; i < min((X % 4) + 4, X); i++)
                for (int j = 0; j < L; j++)
                {
                        mul(sum.c_str(), vec[j].c_str(), sum);
                        if ((success == 0 && sum == "i") ||
                                (success == 1 && sum == "k"))
                                success++;
                }
        cout << "Case #" << x << ": " << (success == 2 && sum == "-1" ? "YES" : "NO" )<< endl;
    }
    return 0;
}


