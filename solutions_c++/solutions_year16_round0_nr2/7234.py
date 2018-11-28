#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

long long int flipS(string& s)
{

    long long int n = 0;

    bool flag;
    int i = s.length();
    while(1)
    {
        i--;
        flag = 0;
        if(s[i] == '-')
        {
            //cout << n << endl;
            n++;
            for(int j=0; j<=i; j++)
            {
                if(s[j] == '+')
                {
                    s[j] = '-';
                    flag = 1;
                }
                else
                {
                    s[j] = '+';
                }
            }
            //cout << s << endl;
            //cout << n  << flag << endl;
            if(flag)
                n += flipS(s);
        }
        if(i<0)
            return n;
    }
}

int main()
{

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int t;
    cin >> t;

    string s[t];

    for(int i=0; i<t; i++)
    {
        cin >> s[i];
    }

    for(int i=0; i<t; i++)
    {
        //cout << s[i] << endl;
        cout << "Case #" << i+1 << ": " << flipS(s[i]) << endl;
    }

    return 0;
}
