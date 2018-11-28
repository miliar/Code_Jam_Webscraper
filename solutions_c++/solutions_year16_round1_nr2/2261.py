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
int n;
#define MAXN (100+10)
int a[MAXN][MAXN],deg[2500+10][MAXN]; 
bool b[MAXN]={0};
int r[MAXN]={0},l[MAXN]={0},u;
bool FLA=0;
bool OK=0;
void pri() {
	For(i,n) if (!r[i]) {
		For(j,n) cout<<' '<<a[l[j]][i];
		cout<<endl;OK=1;
		return;
	}
	For(i,n) if (!l[i]) {
		For(j,n) cout<<' '<<a[r[j]][i];
		cout<<endl;OK=1;
		return;
	}
}
void check(int i) {
	if (i>n) {
		pri();return;
	}
	if (!FLA) {
		FLA=1;r[i]=0;check(i+1);FLA=0; 
		if (OK) return;
	}
	For(k,2*n-1) {
		if (b[k]) continue;
		bool flag=0;
		For(j,n) {
			if (l[j]==0) continue;
			if (a[k][j] != a[l[j]][ i ]) {
				flag=1;break;
			}
		}
		if (!flag) {
			b[k]=1;
			r[i]=k;
			check(i+1);
			b[k]=0;
			if (OK) return;
		}
	}
}
void find(int j) {
	if(j>n) {
//		For(i,n) cout<<l[i]<<' ';
//		cout<<endl;
//		cout<<u<<endl;
		r[1]=u;
		check(2);
		return ;
	} 
	if(j==1) {
		
		if (!FLA) {
			FLA=1;l[j]=0;find(j+1);FLA=0; 
			if (OK) return;
		}
	}
	For(i,deg[a[u][j]][0]) {
		int p=deg[a[u][j]][i];
		if (b[p]) continue;
		b[p]=1;
		l[j]=p;
		find(j+1);
		b[p]=0;
		if (OK) return;
	}
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int T=read();
	For(kcase,T) {
		printf("Case #%d:",kcase);
		cin>>n;
		MEM(deg)
		For(i,2*n-1) {
			For(j,n) a[i][j]=read();
			deg[ a[i][1] ][++deg[a[i][1] ][0] ] = i;
		}
		MEM(b) OK=0;
		For(i,2*n-1) {
			MEM(l)
			b[i]=1;
			u=i;
			find(1);
			b[i]=0;
		}
	} 
	
	return 0;
}

