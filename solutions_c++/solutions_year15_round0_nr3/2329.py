#include<bits/stdc++.h>
using namespace std;

#define p(n) printf("%d\n",n)
#define r(n) scanf("%d",&n)
#define rs(n) scanf("%s",n)
#define ps(n) printf("%s\n",n)
#define P printf
#define R scanf
#define F first
#define S second
#define fr(i,a,b) for(int i=(int)a; i <= (int)b; i++)
#define frr(i,a,b) for(int i=(int)a; i >= (int)b; i--)
#define ll long long int
#define pb push_back
#define vi vector<int>
#define ve(x) vector<x>
#define si set<int>
#define itv vi :: iterator
#define ixv(x) vector<x> :: iterator
#define its si :: iterator
#define ixs(x) set<x> :: iterator
#define fill(s,v) memset(s,v,sizeof(s))
#define all(s) s.begin(),s.end()
#define fs(i,s) for(its i = s.begin(); i != s.end(); i++)
#define fv(i,v) for(itv i = v.begin(); i != v.end(); i++)
#define INF INT_MAX
#define MOD 1000000007
#define ii pair<int,int>
#define mp make_pair
int m[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
char st[100006];
char s[100006];
int func1()
{
    int i,len,f=1;
    len=strlen(st);
    fr(i,0,len-1)
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
int func_aux1(int start)
{
    int i,len,f=1;
    len=strlen(st);
    for(i =start;i <= len-1;i++)
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
int func_aux2(int start)
{
    int len,f=1;
    len=strlen(st);
    fr(i,start,len-1)
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
    int t,k;
    r(t);
    while(t--)
    {
        int x,l,o,ans=1;
        r(l);r(x);
        rs(s);
        o=0;
        fr(i,0,x-1)
        {
            fr(j,0,l-1)
            {
                st[o++]=s[j];
            }
        }
        st[o++]='\0';
        l=func1();
        if(l<0)
            ans=0;
        else
            l=func_aux1(l);
        if(l<0)
            ans=0;
        else
            l=func_aux2(l);
        if(l<0)
            ans=0;
        P("Case #%d: ",k);
        k++;
        if(ans==0)
            ps("NO");
        else
            ps("YES");
    }
    return 0;
}


