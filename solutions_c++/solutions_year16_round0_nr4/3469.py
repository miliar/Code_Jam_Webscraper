#include <iostream>
#include<stdio.h>
#include<string.h>
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
int main()
{
//    freopen("input.txt","r",stdin);
    freopen("input.in","r",stdin);
    freopen("outputt.txt","w",stdout);
    int test;
    ll n,ans,temp,c,k,s;
    cin>>test;
    for(int t=0;t<test;t++)
    {
        cin>>k>>c>>s;
        printf("Case #%d: ",t+1);

/*        for(ll i=1;i<=k;i++)
            cout<<i<<" ";
        cout<<endl;
 */
        if(s<(k+1)/2 || (c==1 && s!=k))
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            if(c==1)
            {
                for(ll i=1;i<=k;i++)
                    cout<<i<<" ";
                cout<<endl;
            }
            else{
            temp=power(k,c-1);
            n=0;
            for(ll i=1;i<=(k+1)/2;i++)
            {
                if(i==(k+1)/2 && k%2==1)
                    cout<<n+i*2-1<<" ";
                else
                cout<<n+i*2<<" ";
                n+=2*(temp);
            }
            cout<<endl;
            }
        }
    }
  //  cout << "Hello world!" << endl;
    return 0;
}
