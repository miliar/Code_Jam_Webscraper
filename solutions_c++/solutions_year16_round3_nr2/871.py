#include <bits/stdc++.h>

#define REP(i,n)        for(i=0;i<n;i++)
#define FOR(i,a,b)      for(i=a;i<=b;i++)
#define DEC(i,a,b)      for(i=a;i>=b;i--)
#define SKIP(i,a,b,k)   for(i=a;i<=b;i+=k)
#define BACK(i,a,b,k)   for(i=a;i>=b;i-=k)
#define ALL(x)          for(auto it=x.begin();it!=x.end();++it)
#define VIT(i,V)        for(i=0;i<V.size();i++)

#define SF          scanf
#define SI(x)       scanf("%d",&x)
#define SI2(x,y)    scanf("%d %d",&x,&y)
#define SI3(x,y,z)  scanf("%d %d %d",&x,&y,&z)
#define SL(x)       scanf("%lld",&x)
#define SL2(x,y)    scanf("%lld %lld",&x,&y)
#define SL3(x,y,z)  scanf("%lld %lld %lld",&x,&y,&z)
#define SD(x)       scanf("%lf",&x)
#define SD2(x,y)    scanf("%lf %lf",&x,&y)
#define SD3(x,y,z)  scanf("%lf %lf %lf",&x,&y,&z)
#define SC(x)       scanf(" %c",&x)
#define SS(x)       scanf("%s",x)
#define PF          printf
#define PI(x)       printf("%d ",x)
#define PI2(x,y)    printf("%d %d ",x,y)
#define PI3(x,y,z)  printf("%d %d %d ",x,y,z)
#define PL(x)       printf("%lld ",x)
#define PL2(x,y)    printf("%lld %lld ",x,y)
#define PL3(x,y,z)  printf("%lld %lld %lld ",x,y,z)
#define PD(x)       printf("%lf ",x)
#define PD2(x,y)    printf("%lf %lf ",x,y)
#define PD3(x,y,z)  printf("%lf %lf %lf ",x,y,z)
#define PC(x)       printf("%c ",x)
#define PS(x)       printf("%s ",x)
#define NL          printf("\n")
#define DEBUG       printf("OK\n")

#define getA(array,size,format) for(int ind=0;ind<size;ind++) scanf(format,array+ind)
#define putA(array,size,format) for(int ind=0;ind<size;ind++) printf(format,*(array+ind))
#define maxA(array,size)        *max_element(array,array+size)
#define minA(array,size)        *min_element(array,array+size)
#define setA(array,size,value)  for(int ind=0;ind<=size;ind++) array[ind]=value
#define setM(array,value)       memset(array,value,sizeof(array))

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define SQR(x)   (x)*(x)
#define MOD(a,b) ((a)%(b)+(b))%(b)
#define GCD(a,b) __gcd(a,b)
#define LCM(a,b) (a)*(b)/__gcd(a,b)
#define lg(n) LOG.at[n]

#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
#define PP pair
#define VC vector
#define S stack
#define Q queue

#define itr iterator
#define pb push_back
#define mp make_pair
#define st first
#define nd second

#define N 100009 ///1e5+9
#define M 200009 ///2e5+9
#define LG 30
#define mod 1000000007 ///1e9+7
#define inf 2000000000 ///2e9

using namespace std;

typedef int I;
typedef long long LL;
typedef double DB;
typedef string STR;

void initial()
{

}

int a[100][100];
LL pw[100];
void solve()
{
    int i,j,x;
    LL n,t,k;
    SL2(n,t); //PL2(n,t);NL;
    if(1LL<<(n-2LL)<t) PF("IMPOSSIBLE\n");
    else{
        PF("POSSIBLE\n");
        t--;
        setM(a,0);
        FOR(i,1,(int)n-2){
            FOR(j,i+1,(int)n-1)
                a[i][j]=1;
        }
        a[0][n-1]=1;
        x=i=(int)n-2;
        while(t>0){
            //PL(t); PI(i);
            if(t%2LL){
                a[0][i]=1;
                x=i;
            }
            t/=2LL; i--;
        }
        FOR(i,1,x-1) setM(a[i],0);
        REP(i,(int)n){ putA(a[i],(int)n,"%d");NL;}
    }
}

int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("output.txt","w",stdout);
	int i,T=1;
	//initial();
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
