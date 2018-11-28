#include <bits/stdc++.h>

#define pi 2*acos(0)
#define INF 1e18
#define MIN 1e-9
#define S(a) scanf("%d",&a)
#define SS(a,b) scanf("%d %d",&a,&b)
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define m_p make_pair
#define p_b push_back
#define n_p(a) next_permutation(all(a))
#define all(v) v.begin(),v.end()
#define allr(v) v.rbegin(),v.rend()
#define ii pair<int, int>
#define vi vector<int>
#define vii vector<ii>
#define rev(s) reverse(all(s))
#define ull unsigned long long
#define ll long long
#define mod 1000000007
#define mem(a,k) memset(a,k,sizeof a)
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)
#define u_b(X,V) upper_bound(X.begin(),X.end(),V)
#define l_b(X,V) lower_bound(X.begin(),X.end(),V)
#define cnt(s,c) count(all(s),c)

using namespace std;

ll _sieve_size;
bitset<10000010> bs;   // 10^7 should be enough for most cases
vi primes;   // compact list of primes in form of vector<int>

void sieve(ll upperbound) {          // create list of primes in [0..upperbound]
  _sieve_size = upperbound + 1;                   // add 1 to include upperbound
  bs.set();                                                 // set all bits to 1
  bs[0] = bs[1] = 0;                                     // except index 0 and 1
  for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
    // cross out multiples of i starting from i * i!
    for (ll j = i * i; j <= _sieve_size; j += i)
		bs[j] = 0;
    primes.push_back((int)i);  // also add this vector containing list of primes
} }

bool isPrime(ll N) {                 // a good enough deterministic prime tester
  if (N <= _sieve_size) return bs[N];                   // O(1) for small primes
  for (int i = 0; i < (int)primes.size(); i++)
    if (N % primes[i] == 0) return false;
  return true;                    // it takes longer time if N is a large prime!
} 

int arr[11];

int n,m,cn;

int check(string s){
	int i,j;

	ll ap[11];

	for(i=2;i<=10;i++){
		ll res=0;
		for(j=0;j<n;j++){
			res=i*res+((s[j]=='1')?(1):(0));
		}
		//cout<<res<<endl;
		if(isPrime(res)){
			return 0;
		}
		ap[i]=res;
	}

	for(i=2;i<=10;i++){
		for(j=0;j<primes.size();j++){
			if(ap[i]%primes[j]==0){
				arr[i]=primes[j];
				break;
			}
		}
	}

	return 1;
}

void build(string s){

	if(s.size()>n||cn==m)
		return;
	if(s.size()==n&&s[n-1]!='0'){
		//cout<<s<<endl;
		if(check(s)){
			cout<<s<<" ";
			for(int i=2;i<=10;i++){
				cout<<arr[i]<<" ";
			}
			cout<<endl;
			++cn;
		}

	}

	build(s+'0');
	build(s+'1');
}


int i,j,k,t,ans,p;

int main(){

	ios_base::sync_with_stdio(0);
	static const size_t npos = -1;
	//istringstream iss(s,istringstream::in);
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);			


	sieve(10000001);


	cin>>t;

	p=1;
	
	while(t--){
		cin>>n>>m;
		cn=0;
		cout<<"Case #"<<p<<":"<<endl;
		build("1");
		++p;
	}
	

	return 0;
}

