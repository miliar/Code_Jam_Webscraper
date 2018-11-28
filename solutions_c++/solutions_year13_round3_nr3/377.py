#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

struct node
{
    int date;
    int a,b;
    int s;
} att[10000];
bool cmp(node a,node b)
{
    return a.date<b.date;
}
int wall[10000];
int walltmp[10000];
int mid=1000;

int main()
{
    freopen("d:\\C-small-attempt0.in","r",stdin);
    freopen("D:\\output.txt","w",stdout);
    int t;
    int N,d,deltad,s,deltas,n,w,e,deltap;
    scanf("%d",&t);
    for(int cas=1; t--; cas++)
    {
        int ans=0;
        int cnt=0;
        memset(wall,0,sizeof(wall));
        memset(walltmp,0,sizeof(walltmp));
        scanf("%d",&N);
        while(N--)
        {
            scanf("%d%d%d%d%d%d%d%d",&d,&n,&w,&e,&s,&deltad,&deltap,&deltas);
            for(int i=0; i<n; i++)
            {
                att[cnt].date=d;
                att[cnt].s=s;
                att[cnt].a=w;
                att[cnt].b=e;
                cnt++;

                d+=deltad;
                w+=deltap;
                e+=deltap;
                s+=deltas;
            }
        }
        sort(att,att+cnt,cmp);
        for(int i=0; i<cnt; i++)
        {
            bool flag=false;
            int a=att[i].a*2+mid;
            int b=att[i].b*2+mid;
            int s=att[i].s;
            for(int i=a; i<=b; i++)
            {
                if(wall[i]<s)
                {
                    flag=true;
                    walltmp[i]=max(walltmp[i],s);
                }
            }
            if(flag) ans++;
            if(i+1<cnt && att[i+1].date!=att[i].date)
            {
                for(int j=0;j<=3000;j++)
                    wall[j]=walltmp[j];
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
}
