#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define ll long long int

using namespace std;
ll a[11];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    // std::ios_base::sync_with_stdio(false);
    ll t,cases=1,n,i,j,m,flag=0,carry;


    cin>>t;
    while(t--)
    {
        cin>>n;
        memset(a,0,sizeof(a));
        cout<<"Case #"<<cases<<": ";
        cases++;
        flag = 0;
        int c=1;
        m=n;
        if(n==0) cout<<"INSOMNIA"<<endl;
        else{
            while(1){
                n = m;
                n*=c;
                carry = n;
                //cout<<"N: "<<n<<" Carry: "<<carry<<endl;
                flag = 0;
                while(n!=0)
                {
                    ll ret = n%10;
                    //cout<<"RET: "<<ret<<endl;
                    a[ret] = 1;
                    n/=10;
                }
                for(i=0;i<=9;i++)
                {
                    //cout<<"A: "<<a[i]<<endl;
                    if(a[i]!=1){
                        flag = 1;
                        break;
                    }
                }
                if(flag==0){
                    cout<<carry<<endl;
                    break;
                }
                c++;
            }

        }
    }


    return 0;
}
