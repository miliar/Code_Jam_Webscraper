//This is the painkiller...
#include<stdio.h>
#include<iostream>
#include<sstream>
#include<queue>
#include<math.h>
#include<stdlib.h>
#include<stack>
#include<string.h>
#include<string>
#include<map>
#include<algorithm>
#include<time.h>
#include<set>
#include<vector>
using namespace std;
#define fin(a) freopen(a,"r",stdin)
#define fout(a) freopen(a,"w",stdout)
#define abv(a) ((a)>0?(a):-(a))
#define sqr(a) ((a)*(a))
#define fs(i,s) for(int i=0;s[i];i++)
#define fg(e,u) for(int e=L[u];e!=-1;e=pre[e])
#define f0(i,n) for(int i=0;i<(n);i++)
#define f1(i,a,n) for(int i=(a);i<(n);i++)
#define f2(i,a,n,b) for(int i=(a);i<(n);i+=(b))
#define rf0(i,n) for(int i=(n);i>=0;i--)
#define rf1(i,a,n) for(int i=(a);i>(n);i--)
#define rf2(i,a,n,b) for(int i=(a);i>(n);i-=(b))
#define mem(a,v) memset(a,v,sizeof(a))
#define pq priority_queue
#define pb push_back
#define pq priority_queue
#define sz size
#define vint vector<int>
#define vvint vector<vector<int> >
#define vstr vector<string>
#define emt empty
#define clr clear
#define bn begin
#define en end
#define all(a) a.bn(),a.en()
#define dlt(v,a) v.erase(v.bn()+a)
#define dlst(v) v.erase(v.bn()+((int)v.size()-1))
#define nset(S,v) S.erase(find(v))
#define scn(a,b,n) f1(j,b,n+b)cin>>a[j]
#define scm(a,b,c,m,n) f1(i,b,m+b)scn(a[i],c,n)
#define prn(a,b,n) f1(j,b,n+b){if(j>b)cout<<' ';cout<<a[j];}
#define prm(a,b,c,m,n) f1(i,b,m+b){prn(a[i],c,n);cout<<endl;}
#define greater(a,b) ((a)>(b)+eps)
#define zero(a) (fabs(a)<eps)
#define Int __int64
#define Long long long
const double Pi=acos(-1.0);
Long mod=1000000007;
#define inf (1<<30)
#define eps 1e-9
#define MAX 1005
//struct pii{int x,y;pii(int a=0,int b=0){x=a,y=b;}};
//bool operator<(pii a,pii b){return a.x<b.x||(a.x==b.x&&a.y<b.y);}
//int L[],pre[],to[],C[],ne;
//inline void addEdge(int u,int v,int c=1){to[ne]=v,pre[ne]=L[u],C[ne]=c;L[u]=ne++;}
int A[105][105];bool flag[105];
char ans[2][4]={"NO","YES"};
int main()
{
    //ios_base::sync_with_stdio(false);
    //fin("in.txt");
    //fout("out.txt");
    /*fout("in.txt");puts("100");f0(t,100){puts("100 100");
    f0(i,100){f0(j,100)printf(" %d",i+1);puts("");}}return 0;*/
    int tst,cas=0;scanf("%d",&tst);
    while(tst--)
    {
        int m,n;scanf("%d%d",&m,&n);
        f0(i,m)f0(j,n)scanf("%d",&A[i][j]);
        mem(flag,false);
        f0(i,m)f0(j,n)flag[A[i][j]]=true;
        vint r,c,v;
        f1(i,1,100)if(flag[i])v.pb(i);v.pb(100);
        //puts("ok");
        f0(t,(int)v.sz()-1)
        {
            int h=v[t];
            r.clr();c.clr();
            f0(i,m)
            {
                bool f=1;
                f0(j,n)
                    if(A[i][j]!=h)f=0;
                if(f)r.pb(i);
            }
            f0(j,n)
            {
                bool f=1;
                f0(i,m)
                    if(A[i][j]!=h)f=0;
                if(f)c.pb(j);
            }
            f0(i,r.sz())f0(j,n)A[r[i]][j]=v[t+1];
            f0(i,c.sz())f0(j,m)A[j][c[i]]=v[t+1];
        }
        //puts("ok");
        int f=1;
        f0(i,m)f0(j,n)if(A[i][j]!=100){f=0;goto hell;}
        //puts("ok");
        hell:;
        printf("Case #%d: %s\n",++cas,ans[f]);
    }
	return 0;
}
