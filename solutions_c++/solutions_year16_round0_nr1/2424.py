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

vector <int> ans;

int main(){
	for(int i=1; i<=1000000; i++){
		set <int> S;
		int curr=i;
		while(true){
			int curr1=curr;
			while(curr1){
				S.insert(curr1%10);
				curr1/=10;
			}
			if(S.size()==10)break;
			curr+=i;
		}
		ans.pb(curr);
	}
	int t,n;
	sc("%d", &t);
	for(int T=1; T<=t; T++){
		sc("%d", &n);
		pr("Case #%d: ", T);
		if(n==0){
			pr("INSOMNIA\n");
		}
		else pr("%d\n", ans[n-1]);
	}
	return 0;
}