# include <bits/stdc++.h>
using namespace std;
ifstream fi("b.in");
ofstream fo("b.out");
int get(string s,char key)
{
    if (s.length() == 1) return s[0] != key;
    if (s[s.length() - 1] == key)
    {
        s.erase(s.end() - 1);
        return get(s,key);
    }
    else
    if (s[0] != key)
    {
        reverse(s.begin(),s.end());
        for (int i = 0;i < s.length();++i)
            if (s[i] == '+') s[i] = '-';else s[i] = '+';
        return 1 + get(s,key);
    }
    else
    {
        while (s.length() && s[s.length() - 1] != key) s.erase(s.end() - 1);
        reverse(s.begin(),s.end());
        for (int i = 0;i < s.length();++i)
            if (s[i] == '+') s[i] = '-';else s[i] = '+';
        return 2 + get(s,key == '+' ? '-':'+');
    }
}
int main(void)
{
    int t;
    fi>>t;
    for (int cs = 1;cs <= t;++cs)
    {
        fo << "Case #" << cs << ": ";
        string s;
        fi>>s;
        fo << get(s,'+') << '\n';
    }
    return 0;
}
