#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
    int t, smax;
    int shy[1011];
    char s[1011];

    //freopen("A-large.in","r",stdin);
    //freopen("out.out","w",stdout);

    cin >> t;
    for (int tc = 1; tc <= t; tc++)
    {
        cin>>smax;
        for(int i = 0; i <= smax; i++)
        {
            cin>>s[i];
            shy[i] = s[i] - '0';
        }


        int stdnAud = 0;
        int frnd = 0;
        for(int i = 0; i < smax; i++)
        {
            stdnAud += shy[i];
            if (stdnAud < i + 1)
            {
                frnd += i - stdnAud + 1;
                stdnAud++;
            }
        }
        cout<<"Case #"<<tc<<": "<<frnd<<"\n";


    }
}
