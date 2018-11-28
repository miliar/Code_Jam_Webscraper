#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
#define fill(s,v) memset(s,v,sizeof(s))
#define fs first
#define sf second
#define pb push_back
#define mkp make_pair

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("outputr1.txt", "w", stdout);
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int d,i,j=0,ans=0,a[1003],st[1003],temp=0;int x,y;
        cin>>d;
        int p[d];
        fill(a,0);
        fill(st,0);
        for(i=0;i<d;i++)
        {
            cin>>p[i];
            a[p[i]]++;
            st[p[i]]++;
        }
        sort(p,p+d);
        ans=p[d-1];
        for(i=p[d-1];i>0;i--)
        {
            if(a[i]!=0)
            {
                if(ans>temp+i)
                    ans=temp+i;
                temp+=a[i];
                if(i%2==0)
                {
                    a[i/2]+=2*a[i];
                }
                else
                {
                    x=i/2-1;
                    y=i/2+2;
                    if(x==1||x==0)
                    {
                        a[i/2]+=a[i];
                        a[i/2+1]+=a[i];
                    }
                    else
                    {
                        a[x]+=a[i];
                        a[y]+=a[i];
                    }
                }
                a[i]=0;
            }
        }
        int mi=ans;
        for(i=0;i<1003;i++)
            a[i]=st[i];
        ans=p[d-1];temp=0;
        for(i=p[d-1];i>0;i--)
        {
            if(a[i]!=0)
            {
                if(ans>temp+i)
                    ans=temp+i;
                temp+=a[i];
                if(i%2==0)
                {
                    a[i/2]+=2*a[i];
                }else
                {
                    a[i/2]+=a[i];
                    a[i/2+1]+=a[i];
                }
                a[i]=0;
            }
        }
        //cout<<"dono sahi"<<ans<<"\n";
        mi=min(ans,mi);
        for(i=0;i<1003;i++)
            a[i]=st[i];
        temp=0;
        ans=p[d-1];
        for(i=p[d-1];i>0;i--)
        {
            if(a[i]!=0)
            {
                if(ans>temp+i)
                    ans=temp+i;
                temp+=a[i];
                if(i%2==0)
                {
                    x=i/2-1;
                    y=i/2+1;
                    if(x==1||x==0)
                        a[i/2]+=2*a[i];
                    else
                    {
                        a[x]+=a[i];
                        a[y]+=a[i];
                    }
                }
                else
                {
                    x=i/2-1;
                    y=i/2+2;
                    if(x==1||x==0)
                    {
                        a[i/2]+=a[i];
                        a[i/2+1]+=a[i];
                    }
                    else
                    {
                        a[x]+=a[i];
                        a[y]+=a[i];
                    }
                }
                a[i]=0;
            }
        }
        mi=min(ans,mi);
        for(i=0;i<1003;i++)
            a[i]=st[i];temp=0;
        ans=p[d-1];
        for(i=p[d-1];i>0;i--)
        {
            if(a[i]!=0)
            {
                if(ans>temp+i)
                    ans=temp+i;
                temp+=a[i];
                if(i%2==0)
                {
                    x=i/2-1;
                    y=i/2+1;
                    if(x==1||x==0)
                        a[i/2]+=2*a[i];
                    else
                    {
                        a[x]+=a[i];
                        a[y]+=a[i];
                    }
                }
                else
                {
                    x=i/2;
                    y=i/2+1;
                        a[x]+=a[i];
                        a[y]+=a[i];
                }
                a[i]=0;
            }
        }
        mi=min(ans,mi);
       cout<<"Case #"<<k<<": "<<mi<<"\n";
    }
    return 0;
}

