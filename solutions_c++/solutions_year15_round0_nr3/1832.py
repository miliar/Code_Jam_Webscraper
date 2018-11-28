#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<map>
using namespace std;
int mul[8][8]={0,1,2,3,4,5,6,7,1,4,3,6,5,0,7,2,2,7,4,1,6,3,0,5,3,2,5,4,7,6,1,0,4,5,6,7,0,1,2,3,5,0,7,2,1,4,3,6,6,3,0,5,2,7,4,1,7,6,1,0,3,2,5,4};
typedef struct Pair
{
        int x,y;
        Pair(int x=0,int y=0):x(x),y(y){}
        friend bool operator < (Pair a,Pair b)
        {
            return a.x==b.x?a.y<b.y:a.x<b.x;
        }
} Pair;
int s[10005],n,wh[4],m;
int a[10005];
int b[10005];
map<Pair,bool> mp[2];
bool v[10][10][10];
void f()
{
    memset(v,0,sizeof(v));
    mp[0].clear();mp[1].clear();
    a[0]=s[0];
    for(int i=1;i<n;i++)
        a[i]=mul[a[i-1]][s[i]];
    b[n-1]=s[n-1];
    for(int i=n-2;i>=0;i--)
        b[i]=mul[s[i]][b[i+1]];
    int x=0;
    for(int i=1;i<n-1;i++,x^=1)
    {
            mp[x^1].clear();
            for(map<Pair,bool>::iterator it = mp[x].begin();it !=mp[x].end();it++)
            {
                Pair p=(*it).first;
                p.y=mul[p.y][s[i]];
                mp[x^1][p]=1;
                v[p.x][p.y][b[i+1]]=1;
            }
            Pair p = Pair(a[i-1],s[i]);
            mp[x^1][p]=1;
            v[a[i-1]][s[i]][b[i+1]]=1;
    }
}

void input()
{
    scanf("%d%d",&n,&m);
    getchar();
    char ch;
    for(int i=0;i<n;i++)
    {
        scanf("%c",&ch);
        for(int j=0;j<m;j++)
            s[i+n*j]=ch-'i'+1;
    }
    n=n*m;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        input();
        f();
        if(v[1][2][3]) printf("Case #%d: YES\n",++ca);
        else printf("Case #%d: NO\n",++ca);
    }
    return 0;
}
