#include <bits/stdc++.h>
#define pb push_back
#define pii pair <int, int>
#define mp make_pair
#define F first
#define S second
#define ll long long
#define iosbase ios_base::sync_with_stdio(false)
#define sc scanf
#define pr printf
#define null NULL
#define getcx getchar_unlocked
#define lb lower_bound
#define ub upper_bound
#define all(x) x.begin(), x.end()
#define pll pair<ll,ll>
#define vi vector <int>
#define vll vector <ll>
 
#define maxs 200005
#define logmaxs 25
 
#define MOD 1000000007
#define eps 1e-9
#define llmax 1e18+5
#define intmax 1e9+5
#define intmin -intmax

#define pi 3.14159265358979

using namespace std;

string s1[50], s2[50];

int s[50];
int ans;

void eval(int n){
	set <string> a,b;
	for(int i=0; i<n; i++){
		if(s[i]==1){
			a.insert(s1[i]);
			b.insert(s2[i]);
		}
	}
	int fl=true;
	int cnt=0;
	for(int i=0; i<n; i++){
		if(s[i]==0){
			cnt++;
			if(a.find(s1[i])==a.end() || b.find(s2[i])==b.end()){
				fl=false;
				break;
			}
		}
	}
	if(fl)
	ans=max(ans, cnt);
}

void subsets(int i, int n){
	if(i==n){
		eval(n);
		return;
	}
	s[i]=0;
	subsets(i+1, n);
	s[i]=1;
	subsets(i+1, n);
}

int main(){
	iosbase;
	int t;
	cin>>t;

	for(int T=1; T<=t; T++){
		int n;
		cin>>n;
		for(int i=0; i<n; i++){
			cin>>s1[i]>>s2[i];
		}
		memset(s, 0, sizeof s);
		ans=intmin;
		subsets(0, n);
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}