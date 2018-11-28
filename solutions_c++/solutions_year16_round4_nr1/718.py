#include <bits/stdc++.h>
using namespace std;

int n,c[3];
int pp[14];
int d[3];
char ch(int x)
{
    if(x==0) return 'R';
    else if(x==1) return 'P';
    else return 'S';
}
bool w(int x,int h)
{
    if(h==0)
    {
        d[0]=d[1]=d[2]=0;
        w(x,1);
        if(d[0]==c[0] && d[1]==c[1] && d[2]==c[2]) return true;
        else return false;
    }
    if(h==n+1)d[x]++;
    else
    {
        int y=x-1;
        if(x==0) y=2;
        if(ch(x)>ch(y)) swap(x,y);
        w(x,h+1);
        w(y,h+1);
    }
}



int m[10000];
string ans;
string t;

void opti(string &q, int h=1)
{
    if(q.length()==h) return;
    int z = h*2;
    for(int i=0;i<q.length();i+=z)
        if(q.substr(i,h)>q.substr(i+h,h))
    {
        for(int j=0;j<h;++j)
            swap(t[i+j],t[i+h+j]);
    }
    opti(q,z);
}

bool g(int x,int h,int pos=0)
{
    if(h==n+1)m[pos]=x;
    else
    {

        int y=x-1;
        if(x==0) y=2;
        if(ch(x)>ch(y)) swap(x,y);
        g(x,h+1,pos);
        g(y,h+1,pos+pp[n-h]);
    }
    if(h==1)
    {
        t="";
        for(int i=0;i<pp[n];++i)
            t.push_back(ch(m[i]));

        opti(t);

        if(ans=="IMPOSSIBLE") ans=t;
        else
        ans=min(ans,t);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    pp[0]=1;
    for(int i=1;i<14;++i) pp[i]=pp[i-1]*2;
    int T;
    scanf("%d",&T);
    for(int test=1;test<=T;++test)
    {
        printf("Case #%d: ", test);
        ans = "IMPOSSIBLE";
        scanf("%d%d%d%d",&n,&c[0],&c[1],&c[2]);
        if(w(0,0)) g(0,1);
        if(w(1,0)) g(1,1);
        if(w(2,0)) g(2,1);
        printf("%s\n",ans.c_str());
    }

}
