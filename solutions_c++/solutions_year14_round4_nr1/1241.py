#include <bits/stdc++.h>
#define mpr std::make_pair
#define lg std::__lg
#define __count __builtin_popcount
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define pb push_back
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
const int N=100100;
int A[N];
bool flag[N];
int main(){
	//freopen(".in","r",stdin);
	//freopen(".out","w",stdout);
	int T,n,x;
	RI(T);
	int w=1;
	while(T--){
		RI(n,x);
		for(int i=0;i<n;i++)
			RI(A[i]);
		sort(A,A+n);
		int ans=0;
		for(int i=0;i<n;i++)flag[i]=false;
		for(int i=n-1;i>=0;i--) {
			if(flag[i])continue;
			for(int j=i-1;j>=0;j--)
				if(!flag[j]&&A[i]+A[j]<=x) {
					flag[j]=true;
					break;
				}
			ans++;
		}
		printf("Case #%d: %d\n",w++,ans);
	}
	return 0;
}

