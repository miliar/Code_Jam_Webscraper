#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
int m[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
char st[100006];
char s[100006];
int fdi()
{
    int i,len,f=1;
    len=strlen(st);
    for(i=0;i<len;i++)
    {
        if(st[i]=='i')
        {
            if(f>0)
            {
                f=m[f-1][1];
            }
            else
            {
                f=-f;
                f=m[f-1][1];
                f=-f;
            }
        }
        if(st[i]=='j')
        {
            if(f>0)
            {
                f=m[f-1][2];
            }
            else
            {
                f=-f;
                f=m[f-1][2];
                f=-f;
            }
        }
        if(st[i]=='k')
        {
            if(f>0)
            {
                f=m[f-1][3];
            }
            else
            {
                f=-f;
                f=m[f-1][3];
                f=-f;
            }
        }
        if(f==2)
        {
            return i+1;
        }
    }
    if(i==len)
        return -1;
}
int fdj(int start)
{
    int i,len,f=1;
    len=strlen(st);
    for(i=start;i<len;i++)
    {
        if(st[i]=='i')
        {
            if(f>0)
            {
                f=m[f-1][1];
            }
            else
            {
                f=-f;
                f=m[f-1][1];
                f=-f;
            }
        }
        if(st[i]=='j')
        {
            if(f>0)
            {
                f=m[f-1][2];
            }
            else
            {
                f=-f;
                f=m[f-1][2];
                f=-f;
            }
        }
        if(st[i]=='k')
        {
            if(f>0)
            {
                f=m[f-1][3];
            }
            else
            {
                f=-f;
                f=m[f-1][3];
                f=-f;
            }
        }
        if(f==3)
        {
            return i+1;
        }
    }
    if(i==len)
        return -1;
}
int fdk(int start)
{
    int i,len,f=1;
    len=strlen(st);
    for(i=start;i<len;i++)
    {
        if(st[i]=='i')
        {
            if(f>0)
            {
                f=m[f-1][1];
            }
            else
            {
                f=-f;
                f=m[f-1][1];
                f=-f;
            }
        }
        if(st[i]=='j')
        {
            if(f>0)
            {
                f=m[f-1][2];
            }
            else
            {
                f=-f;
                f=m[f-1][2];
                f=-f;
            }
        }
        if(st[i]=='k')
        {
            if(f>0)
            {
                f=m[f-1][3];
            }
            else
            {
                f=-f;
                f=m[f-1][3];
                f=-f;
            }
        }
    }
    if(f==4)
        return 1;
    else
        return -1;
}
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int x,l,i,j,o,ans=1;
        cin>>l>>x;
        cin>>s;
        o=0;
        for(i=0;i<x;i++)
        {
            for(j=0;j<l;j++)
            {
                st[o++]=s[j];
            }
        }
        st[o++]='\0';
        l=fdi();
        if(l<0)
            ans=0;
        else
            l=fdj(l);
        if(l<0)
            ans=0;
        else
            l=fdk(l);
        if(l<0)
            ans=0;
        if(ans==0)
            cout<<"Case #"<<k<<": NO\n";
        else
            cout<<"Case #"<<k<<": YES\n";
    }
    return 0;
}


