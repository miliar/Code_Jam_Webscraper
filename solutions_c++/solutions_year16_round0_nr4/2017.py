#include<iostream>
#include<stdio.h>
using namespace std;
int t,s,num;
long long k,c,i,now;
int main()
{
    //freopen("a.in","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cin>>k>>c>>s;
        if(s*c<k)cout<<"Case #"<<tt<<": IMPOSSIBLE"<<endl;
        else
        {
            cout<<"Case #"<<tt<<':';
            i=1; num=0; now=1;
            while(i<=k)
            {
                now=(now-1)*k+i;
                num++;
                if(num==c){cout<<' '<<now; now=1; num=0;}
                i++;
            }
            if(num>0)
            {
                while(num<c){now=now*k; num++;}
                cout<<' '<<now;
            }
            cout<<endl;
        }
    }
    return 0;
}