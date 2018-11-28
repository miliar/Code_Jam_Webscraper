#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(auto y=x.begin();y!=x.end();y++)
#define pb(f) push_back(f)
#define pi_ printf("\n")
#define pi(a) printf("%d\n",a)
#define pil(a) printf("%lld\n",a)
#define sc(a) scanf("%d",&a)
#define ll long long
#define scl(a) scanf("%lld",&a)
#define scs(a) scanf("%s",a)
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007
#define inf 1000000009
#define maxn 100009
using namespace std;
//#include<windows.h>
FILE *fin = freopen("1.in","r",stdin);
FILE *fout = freopen("out2.txt","w",stdout);
using namespace std;
typedef pair<int,int> pii;
typedef vector<int > vi;
typedef vector< pii > vpii;
int n,k;
double ans=0,a[20],t2=0;void test2(vector<int> &v,int i,double ansa,int p,int np);
void rec2(int tot,int rem,vector<int> v)
{
	if(rem==0)
	{
		t2=0;
	//	for(auto it: v)
	//	cout<<it<<" ";cout<<endl;
		test2(v,k-1,1.00,k/2,k/2);
		ans=max(t2,ans);
		return;
	}
	if(tot<rem)
	return;
	rec2(tot-1,rem,v);
	v.pb(tot);
	rec2(tot-1,rem-1,v);
	
}
void test2(vector<int> &v,int i,double ansa,int p,int np)
{
//	if(i<p||i<np)
//	{
//		return;
//	}
//cout<<p<<" "<<np<<endl;
	if(i<-1)
	return;
	if(i+1<p||i+1<np) return;
	if(p==0&&np==0)
	{
		t2+=ansa;
	//	printf("%lf\n",ansa);
		return;
	}
//	cout<<"vdvdf";
//	cout<<v[i]<<" "<<a[v[i]]<<endl;
	if(p>0)
	test2(v,i-1,ansa*a[v[i]],p-1,np);
	if(np>0)
	test2(v,i-1,ansa*(1.00-a[v[i]]),p,np-1);
}
int main()
{
	int t,i,j,cas=0;
	sc(t);while(t--)
	{
		ans=0;
		cas++;	printf("Case #%d: ",cas);
		sc(n);sc(k);
		rep(i,1,n+1)
		{
			scanf("%lf",&a[i]);
		}
		vector<int> v;
		rec2(n,k,v);
		printf("%lf\n",ans);
	}
}
