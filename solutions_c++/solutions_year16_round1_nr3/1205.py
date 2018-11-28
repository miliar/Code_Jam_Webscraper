#include<bits/stdc++.h>
using namespace std;
#define For(i,n) for(int i=1;i<=n;i++)
#define Fork(i,k,n) for(int i=k;i<=n;i++)
#define Rep(i,n) for(int i=0;i<n;i++)
#define ForD(i,n) for(int i=n;i;i--)
#define ForkD(i,k,n) for(int i=n;i>=k;i--)
#define RepD(i,n) for(int i=n;i>=0;i--)
#define Forp(x) for(int p=Pre[x];p;p=Next[p])
#define Forpiter(x) for(int &p=iter[x];p;p=Next[p])  
#define Lson (o<<1)
#define Rson ((o<<1)+1)
#define MEM(a) memset(a,0,sizeof(a));
#define MEMI(a) memset(a,127,sizeof(a));
#define MEMi(a) memset(a,128,sizeof(a));
#define INF (2139062143)
#define F (100000007)
#define pb push_back
#define mp make_pair 
#define fi first
#define se second
#define vi vector<int> 
#define pi pair<int,int>
#define SI(a) ((a).size())
#define PRi(a,n) For(i,n-1) cout<<a[i]<<' '; cout<<a[n]<<endl;
#define PRi2D(a,n,m) For(i,n) { \
						For(j,m-1) cout<<a[i][j]<<' ';\
						cout<<a[i][m]<<endl; \
						} 
typedef long long ll;
typedef unsigned long long ull;
ll mul(ll a,ll b){return (a*b)%F;}
ll add(ll a,ll b){return (a+b)%F;}
ll sub(ll a,ll b){return (a-b+llabs(a-b)/F*F+F)%F;}
void upd(ll &a,ll b){a=(a%F+b%F)%F;}
int read()
{
	int x=0,f=1; char ch=getchar();
	while(!isdigit(ch)) {if (ch=='-') f=-1; ch=getchar();}
	while(isdigit(ch)) { x=x*10+ch-'0'; ch=getchar();}
	return x*f;
} 
int n,a[1010];
int t[1010];
bool check(int m) {
	For(i,m) {
		int v1=i+1,v2=i-1;
		if (v2==0) v2=m;
		if (v1==m+1) v1=1;
		if (a[t[i]]!=t[v1]&&a[t[i]]!=t[v2]) return 0;
	}
	return 1;
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C2.out","w",stdout);
	int T=read();
	For(kcase,T) {
		printf("Case #%d: ",kcase);
		n=read();
		For(i,n) a[i]=read();
		int ans=0;
		For(i,n) t[i]=i;
		int p=1;
		For(i,n) p*=i;
		
		while(p--) {
//			PRi(t,n)
			Fork(i,2,n) if (check(i)) ans=max(ans,i);
			next_permutation(t+1,t+1+n);
		}
		cout<<ans<<endl;
	} 	
	return 0;
}

