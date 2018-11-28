#include<bits/stdc++.h>

using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<char> vch;
typedef vector<vector<int> > vvi;
typedef map<int,int> MPII;
typedef set<int> SET;
typedef multiset<int> MSET;
 
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define F(i,a,b) for(i=a;i<=b;i++)
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define repn(i,n) F(i,1,n)
#define bit(x,i) ( x & (1 << i) ) 
#define lowbit(x) ((x)&((x)^((x)-1))) //get the lowest bit of x
#define hBit(msb,n) asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x, maybe the fastest
#define fill(a,b)   memset(a,b,sizeof(a)) 
#define sz(a)      (int)(a.size())
#define MIN(a,b)     (a) = min((a),(b))
#define MAX(a,b)     (a) = max((a),(b))
#define ff first
#define ss second
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)
#define M 1000000003
const int N = 1000*100 + 5;
ll pow(ll num,ll power){if(power==0)return 1;if(power==1)return num;	ll t = pow(num,power/2);return power%2?t*t*num:t*t;}
//long dp[1001];
int main()
{	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	//double c1 = clock();
	//*************CODE*****************
	ios::sync_with_stdio(false);
	int t,n,i;string s;
	cin>>t;
	int j = t;
	char ch;
	while(t--){
		cin>>n;
		//cin>>ch;
		cin>>s;
		//dp[0] = s[0] - '0';
		int l = sz(s);
		long sum = s[0]-'0';
		//cout<<n<<" "<<s<<endl;
		//repn(i,l-1) dp[i] = dp[i-1] + (s[i] - '0');
		int ans = 0;
		repn(i,l-1){
			//sum += (s[i] - '0');
			//if(s[i]=='0'){
				if(s[i]=='0') continue;
				if(sum < i) {
				ans += i-sum;
				sum += ans;
				}
			//}
			sum += (s[i] - '0');
			//cout<<sum<<" ";
		}
		cout<<"Case #"<<j-t<<": "<<ans<<endl;
	}
	
	//*************END******************
	//c1 = clock() - c1;
	//fprintf(stderr,"Execution Time = %lf sec\n",c1 / CLOCKS_PER_SEC);
	return 0;
}
