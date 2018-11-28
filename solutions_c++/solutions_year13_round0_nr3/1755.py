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
#define MAX 10000005
//struct pii{int x,y;pii(int a=0,int b=0){x=a,y=b;}};
//bool operator<(pii a,pii b){return a.x<b.x||(a.x==b.x&&a.y<b.y);}
//int L[],pre[],to[],C[],ne;
//inline void addEdge(int u,int v,int c=1){to[ne]=v,pre[ne]=L[u],C[ne]=c;L[u]=ne++;}

int arr[10],L;

int pCheck(Long a)
{
    int sq[20],c=0;
    while(a)sq[c++]=a%10,a/=10;
    f0(i,c/2+1)if(sq[i]!=sq[c-1-i])return 0;
    return 1;
}
vector<Long> V;
void backTrack(int f,int l)
{
    if(f>l)
    {
        Long a=0;
        f0(i,L)a=a*10+arr[i];
        if(pCheck(a*a))V.pb(a*a);
        return;
    }
    f1(i,1,10)
    {
        arr[f]=arr[l]=i;
        backTrack(f+1,l-1);
    }
    if(f!=0)
    {
        arr[f]=arr[l]=0;
        backTrack(f+1,l-1);
    }
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //fin("in.txt");
    //fout("out.txt");
    for(L=1;L<8;L++)backTrack(0,L-1);V.pb(100000000000001L);
    sort(all(V));//prn(V,0,V.sz());cout<<endl<<V.sz()<<endl;
    int tst,cas=0;scanf("%d",&tst);
    while(tst--)
    {
        int c=0,d=0;Long a,b;
        scanf("%lld%lld",&a,&b);
        f0(i,V.sz())
        {
            if(V[i]>=a)
            {
                c=i;
                break;
            }
        }
        f0(i,V.sz())
        {
            if(V[i]>b)
            {
                d=i;
                break;
            }
        }
        printf("Case #%d: %d\n",++cas,d-c);
    }
	return 0;
}
