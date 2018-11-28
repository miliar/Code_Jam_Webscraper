#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;
int bin[11];
int main()
{
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    int t,tt,tot,temp;
    unsigned long long w1,w,ww;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        memset(bin,0,sizeof(bin));
        tot=0;
        cin>>w1;
        cout<<"Case #"<<tt<<": ";
        if(w1==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        w=w1;
        ww=w;
        while(ww)
        {
            temp=ww%10;
            ww/=10;
            if(bin[temp]==0)
            {
                bin[temp]=1;
                tot++;
            }
        }
        while(tot!=10)
        {
            w+=w1;
            ww=w;
            while(ww)
            {
                temp=ww%10;
                ww/=10;
                if(bin[temp]==0)
                {
                    bin[temp]=1;
                    tot++;
                }
            }
        }
        cout<<w<<endl;
    }
    return 0;
}
