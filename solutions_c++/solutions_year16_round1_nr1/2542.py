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

int main(){
	iosbase;
	int t;
	cin>>t;
	string s;
	for(int T=1; T<=t; T++){
		cin>>s;
		string tmp="";
		tmp+=s[0];
		for(int i=1; i<s.size(); i++){
			string tmp1=tmp;
			tmp1+=s[i];
			string tmp2="";
			tmp2+=s[i];
			tmp2+=tmp;
		//	cout<<tmp1<<" "<<tmp2<<endl;
			if(tmp1>tmp2){
				tmp=tmp1;
			}
			else tmp=tmp2;
		}
		cout<<"Case #"<<T<<": "<<tmp<<endl;
	}
	return 0;
}