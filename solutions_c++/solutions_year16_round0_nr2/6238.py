#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    string s;
    cin >> t;
    cin.ignore();
    for(int c=1; c<=t; c++)
    {
        string s;
        getline(cin, s);
        printf("Case #%d: ", c);
        int i=s.length()-1;
        int groups=0;
        char curr = '+';
        while(s[i]=='+')
            i--;
        while(i >= 0)
        {
            if(s[i]!=curr)
            {
                groups++;
                curr = s[i];
            }
            i--;
        }
        printf("%d\n", groups);
    }
    return 0;
}
