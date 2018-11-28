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
int k;
char s[10000];
int a[10000];
int main()
{
//	freopen("A.in","r",stdin);
//	freopen("a.out","w",stdout);
	
	int T=read();
	For(kcase,T) {
		printf("Case #%d: ",kcase); 
		cin>>(s+1)>>k;
		int n=strlen(s+1);
		For(i,n) a[i]=s[i]=='-';
		int p=0;
		For(i,n-k+1) if (a[i]){
			For(j,k) {
				a[i+j-1]^=1;
			}
			++p;
		}
		bool fl=0;
		For(i,n) if (a[i]) {
			p=-1;
		}
		if (p==-1) 	puts("IMPOSSIBLE");
		else cout<<p<<endl;
	}
	
	return 0;
}

