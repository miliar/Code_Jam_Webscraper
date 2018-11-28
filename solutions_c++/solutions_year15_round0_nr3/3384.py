#include <iostream>
#include <algorithm>
#include <memory.h>
using namespace std;

//#define MY_TEST

char all[10007];

inline int numchar(char c)
{
    return ((c-'i')+2);
}
inline int prod(int o,int t)
{
    int res=1;
    if(o<0)
    {
        res*=-1;
        o*=-1;
    }
    if(t<0)
    {
        t*=-1;
        res*=-1;
    }
    if(o==1) return res*t;
    if(t==1) return res*o;
    if(o==t) return res*-1;
    if(o==2 && t==3) return res*4;
    if(o==3 && t==4) return res*2;
    if(o==4 && t==2) return res*3;
    if(o==3 && t==2) return res*-4;
    if(o==4 && t==3) return res*-2;
    if(o==2 && t==4) return res*-3;
    return 0;
}

int main()
{
    #ifndef MY_TEST
    freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    #endif // MY_TEST

    long long T,k,ans,i,j,t,hasi,hask,hasj,cur,r,L,X,s;
    cin>>T;
    for(k=1;k<=T;++k)
    {
        cin>>L>>X;
        cin>>all;
        t=L*X;
       // cout<<t;
        hasi=0;
        hasj=0;
        hask=0;
        ans=0;
        for(j=1;j<X;++j)
        {
            for(i=0;i<L;++i)
            {
                all[(j*L)+i]=all[i];
            }
        }
        all[t]='\0';
     //   cout<<all<<endl;

        cur=numchar(all[0]);                //i=2,j=3,k=4,1=1
        for(j=1;j<t;++j)
        {
            if(cur==2)
            {
                hasi=1;
                break;
            }
            cur=prod(cur,numchar(all[j]));
     //       cout<<cur<<endl;
        }
      //  cout<<"HASi"<<hasi<<" j:"<<j<<endl;
        cur=numchar(all[t-1]);
        for(r=t-2;r>0;--r)
        {
            if(cur==4)
            {
                hask=1;
                break;
            }
            cur=prod(numchar(all[r]),cur);
       //     cout<<cur<<endl;
        }
      //  cout<<"HASk"<<hask<<" r:"<<r<<endl;


        cur=numchar(all[j]);
        for(s=j+1;s<=r;++s)
        {
            cur=prod(cur,numchar(all[s]));
       //     cout<<cur<<endl;
        }
        if(cur==3)
        {
            hasj=1;
        }
        //cout<<hasi<<" "<<hasj<<" "<<hask<<endl;
        ans=hasi & hasj & hask;
        cout<<"case #"<<k<<": "<<(ans?"YES" : "NO")<<endl;
    }
    return 0;
}
