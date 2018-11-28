#include<iostream>
#include<stdio.h>
using namespace std;
int t,num;
long n,now,nn;
bool f[10];
int main()
{
    freopen("a.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cin>>n;
        if(n==0)cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
        else
        {
        num=0;
        now=n;
        for(int i=0;i<=9;i++)f[i]=false;
        while(num<10)
        {
            nn=now;
            while(nn>0)
            {
                if(!f[nn%10]){f[nn%10]=true; num++;}
                nn/=10;
            }
            now+=n;
        }
        cout<<"Case #"<<tt<<": "<<now-n<<endl;
        }
    }
    return 0;
}