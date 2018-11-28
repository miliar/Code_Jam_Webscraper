#include <iostream>
#include<stdio.h>
#include<string.h>
# define ll long long int
using namespace std;

char s[105];
int main()
{
//    freopen("input.txt","r",stdin);
    freopen("input.in","r",stdin);
    freopen("outputt.txt","w",stdout);
    int test;
    ll n,ans,temp;
    cin>>test;
    for(int t=0;t<test;t++)
    {
        ans=0;
        cin>>s;
        n=strlen(s);
        for(int i=n-1;i>=0;i--)
        {
            if(s[i]!='+')
            {
                ans++;
                for(int j=i;j>=0;j--)
                {
                    if(s[j]=='+')
                        s[j]='-';
                        else
                        s[j]='+';
                }
            }
        }
        printf("Case #%d: %lld\n",t+1,ans);
    }
  //  cout << "Hello world!" << endl;
    return 0;
}
