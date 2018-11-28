#include <iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define lld long long int

int main()
{
    lld t,i,l,cnt,n,a,s;
    int mp[10] ={};
    freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>n;
        cout<<"Case #"<<l<<": ";
        if(n==0)
            cout<<"INSOMNIA";
        else
        {
            for(i=0;i<10;i++)
            {
                mp[i]=0;
            }
            cnt=0;
            for(i=1;;i++)
            {
                s=n*i;
                for(;s>0;s/=10)
                {
                    a=s%10;
                    if(mp[a]==0)
                    {
                        mp[a]=1;
                        cnt++;
                    }
                }
                if(cnt==10)
                    break;
            }
             cout<<n*i;
        }
        cout<<endl;
    }
	return 0;
}
