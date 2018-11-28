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

int cnt[26];
int a[10];

int main(){
	int t;
	cin>>t;
	for(int T=1; T<=t; T++){
		string s;
		cin>>s;
		for(int i=0; i<s.size(); i++){
			s[i]=(char)((s[i]-'A')+'a');
		}
		memset(cnt, 0, sizeof cnt);
		for(int i=0; i<s.size(); i++){
			cnt[s[i]-'a']++;
		}
		memset(a, 0, sizeof a);
		a[0]=cnt['z'-'a'];
		a[2]=cnt['w'-'a'];
		a[4]=cnt['u'-'a'];
		a[6]=cnt['x'-'a'];
		a[8]=cnt['g'-'a'];
		a[3]=cnt['h'-'a']-a[8];
		a[5]=cnt['f'-'a']-a[4];
		a[7]=cnt['v'-'a']-a[5];
		a[9]=cnt['i'-'a']-a[5]-a[6]-a[8];
		a[1]=cnt['o'-'a']-a[0]-a[2]-a[4];
		string ans="";
		for(int i=0; i<=9; i++){
			for(int j=0; j<a[i]; j++){
				ans+=(char)(i+'0');
			}
		}
		sort(ans.begin(), ans.end());
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	return 0;
}