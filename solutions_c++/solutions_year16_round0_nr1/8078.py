#include<cstdio>
#include<cstring>
#include<iostream>
#define MAX 100005
using namespace std;
typedef long long int ll;

int main()
{
    freopen("alarge1.in","r",stdin);
    freopen("cjout1.txt","w",stdout);

    ll n;//,iteration=0;
    int t;
    cin>>t;
    for(int i=1;i<=t;++i)
    {
            cin>>n;
            if(n==0)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            else
            {
                bool D[10]={0},yes=false;
                for(int pp=0;pp<10;++pp)
                D[pp]=false;
                int rem=10;
                ll total=0,finalval,tmp;
                for(ll x=1;x<MAX;++x)
                {
                    tmp=total+=n;
                    while(tmp)
                    {
                        if(!D[(tmp)%10])
                        {
                            D[(tmp%10)]=true;
                            --rem;
                        }
                        tmp/=10;
                    }
                    if(rem==0)
                    {
                        yes=true;
    //                        iteration+=x;
  //                  //finalval=x;
                        break;
                    }
                }
                if(yes)
                cout<<"Case #"<<i<<": "<<total<<endl;
                else
                cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            }
    }
//    cout<<"Total iteration : "<<iteration<<endl;
    return 0;
}
