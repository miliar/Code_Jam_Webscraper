#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi  vector<int>
#define pb  push_back
#define mp  make_pair
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define sci(x) scanf("%d",&x);
#define scl(x) scanf("%lld",&x);
#define scs(x) scanf("%s",x);
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 100000000000000000LL
#define LL long long

const int N = 1e5+5;
int a[10005];
int n;
int sm;
bool good(int i,int j){
	int temp1 = a[i];
	int temp2 = a[j];
	if(!temp1 || !temp2){
		return false;
	}
	a[i]--;
	a[j]--;
	int mx = 0;
	for(int jj=0;jj<n;jj++) {
		mx = max(mx,a[jj]);
	}
	a[i]++;
	a[j]++;
	return 2*mx<=(sm-2);
}
bool check(int i){
	int temp1 = a[i];
	a[i]--;
	int mx = 0;
	for(int jj = 0 ; jj < n;jj++){
		mx = max(mx,a[jj]);
	}
	a[i]++;
	return 2*mx<=(sm-1);
}
int main() {
	freopen("inp.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;sci(t);
	int cs = 0;
	while(t--){
		sci(n);
		char c = 'A';
		for(int i = 0 ; i < n ; i++){
			cin >> a[i];
			sm+=a[i];
		}
		printf("Case #%d: ",++cs);
		bool flag ;
		do {
		   flag = false;
		   for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(a[i]+a[j]>=2 && good(i,j)) {
					flag = true;
					a[i]--;
					a[j]--;
					sm-=2;
					printf("%c%c ",'A'+i,'A'+j);
					break;
				}
			  }
		   }
		   if(!flag) {
		    for(int i=0;i<n;i++){
				if(a[i]>=1 && check(i)) {
					flag = true;
					a[i]--;
					sm-=1;
					printf("%c ",'A'+i);
					break;
				}
			  }
		   }
		}while(flag);
		nl;
	}
}