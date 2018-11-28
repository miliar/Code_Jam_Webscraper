#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(void)
{

//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);

    int t;
    cin>>t;

    for(int test = 1; test <= t; test++)
    {
        long long int smax;
        char str[10000];

        cin>>smax;
        cin>>str;

        long long int ans = 0, standing = str[0]-'0';
        for(int i=1; i<=smax; i++)
        {
            int tmp = str[i]-'0';

            if(!tmp)
                continue;

            if( standing >= i)
            {
                standing += tmp;
            }

            else
            {
                ans += abs(i-standing);
                standing += tmp + abs(i-standing) ;
            }
        }

        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}
