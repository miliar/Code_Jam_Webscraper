#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    freopen("in2.in","r",stdin);
    freopen("ans2.txt","w",stdout);
    long long int t,n,temp[10],ans=0,dummy,mul=1;
    cin>>t;
    for(long long int i = 1 ; i<=t ; ++i)
    {

        mul = 1;
        ans = 0;
        cin>>n;
        if(n == 0){cout<<"Case #"<<i<<": INSOMNIA\n";continue;}
        dummy=n;
        for(int j = 0 ; j < 10 ; ++j){temp[j] = 0;}
        do
        {
            ans =0;
                while(dummy != 0){temp[dummy%10]++;dummy = dummy/10;}
                for(int j = 0 ; j < 10 ; ++j){if(temp[j]==0){ans=1;}}

                if(ans == 1)
                {
                    ++mul;
                    dummy = n*mul;
                }
        }while(ans == 1);
        cout<<"Case #"<<i<<": "<<(n*mul)<<endl;
    }
    return 0;
}
