#include <iostream>
#include<stdio.h>
#include<string.h>
#include<bitset>
# define ll long long int
using namespace std;

ll power(ll x, ll y)
{
    ll temp;
    if( y == 0)
       return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
    {
        if(y > 0)
            return x*temp*temp;
        else
            return (temp*temp)/x;
    }
}
char s[1005];
char f[2005];
int main()
{
 //   freopen("input.txt","r",stdin);
    freopen("input.in","r",stdin);
  freopen("outputtbcc.txt","w",stdout);
    int test;
    int n,ans,temp,c,k,start,end;
    cin>>test;
    for(int t=0;t<test;t++)
    {
        cin>>s;
        n=strlen(s);
        printf("Case #%d: ",t+1);
        start=1002;end=start+n;
        f[start]=s[0];
        for(int i=1;i<n;i++)
        {
            if(s[i]>=f[start])
            {
                start--;end--;
                f[start]=s[i];
            }
            else
            {
                f[start+i]=s[i];
            }
        }
        for(int i=start;i<end;i++)
            cout<<f[i];
        cout<<endl;
    }
  //  cout << "Hello world!" << endl;
    return 0;
}
