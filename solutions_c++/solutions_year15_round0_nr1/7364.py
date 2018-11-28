/*
*************************************
	Author  : prathikyr			
	Team 	: Emptyknapsack				
	Contest : Google Codejam
*************************************
*/
#include<bits/stdc++.h>

#define sd(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define pd(n) printf("%d", n)
#define pl(n) printf("%lld", n)
#define PN printf("\n")
#define ARR_SIZE(arr) (sizeof(arr)/sizeof(arr[0]))
#define MOD 1000000007
#define PB push_back
#define MP make_pair
#define DEBUG(x) cout << #x << " = "; cout << x << endl;
#define PR(a,n) cout << #a << " = "; for(int i=0; i<n; i++) cout << a[i] << ' '; cout << endl;
#define INP(a,n) for(int i=0; i<n; i++) sd(a[i]) ;
#define INPL(a,n) for(int i=0; i<n; i++) sl(a[i]) ;

using namespace std;

const double PI = acos(-1.0);

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ull> vull;
typedef pair<int,int> pii;

int kase=1;

int solve(){
	int c=0, sum=0, i, n;
	char s[1002];
	scanf("%d", &n);
	scanf("%s", s);
	for(i=0; s[i]; i++){
		if(sum<i){
			c=c+(i-sum);
			sum+=((i-sum)+(s[i]-'0'));
		}
		else
			sum+=(s[i]-'0');
	}
	cout<<"Case #"<<kase<<": "<<c<<"\n";
	kase++;
	return 0;
}

int main(){
	ios_base::sync_with_stdio(false);
	int i, t;
	scanf("%d", &t);
	while(t--)
		solve();
	return 0;
}
