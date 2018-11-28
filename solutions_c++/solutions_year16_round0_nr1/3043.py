#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i < (n);i++)
#define range(i,a,b) for(int i = (a);i <= (b);i++)
#define rrep(i,n) for(int i = (n);i >= 0;i--)
#define rran(i,a,b) for(int i = (b);i >= (a);i--)
#define step(i,a,b,d) for(int i = (a);i <= (b); i += d)
#define all(A) A.begin(),A.end()
#define PI acos(-1)
#define pb push_back
#define mp make_pair
#define sz(A) A.size()
#define len(A) A.length()
#define vi vector<int>
#define ll long long
#define pi pair<int,int>
#define point pair<double,double>
#define pl pair<ll,ll>
#define popcnt(x) __builtin_popcount(x)
#define LSOne(x) ((x) & (-(x)))
#define xx first
#define yy second
#define PQ priority_queue
#define print(A,t) cerr << #A << ": "; copy(all(A),ostream_iterator<t>(cerr," " )); cerr << endl
#define prp(p) cerr << "(" << (p).first << " ," << (p).second << ")";
#define prArr(A,n,t)  cerr << #A << ": "; copy(A,A + n,ostream_iterator<t>(cerr," " )); cerr << endl
#define pre() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
using namespace std;

const int MAX = 1 << 20;
int ans[MAX];
int V[10];

int main(){
	range(i,1,MAX){
		int j = i,ctr = 0;  fill(V,V + 10,0);
		while(ctr < 10){
			int k = j;
			while(k){
				int d = k%10; k /= 10;
				if(!V[d]) ctr++;
				V[d] = 1;
			}
			j += i;
		}
		ans[i] = j - i;
	}
	int T,n;
	scanf("%d",&T);
	loop(t,T){
		scanf("%d",&n);
		printf("Case #%d: ",t + 1);
		if(n == 0) puts("INSOMNIA");
		else printf("%d\n",ans[n]);
	}		
	return 0;
}
