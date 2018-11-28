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

int s[8];

string s1,s2;
int mn;
int sc1, sc2;
string ans1, ans2;

int atoi(string s){
	int ret=0;
	for(int i=s.size()-1, j=0; i>=0; i--, j++){
		ret+=(s[i]-'0')*(pow(10, j));
	}
	return ret;
}

void eval(int n){
	string t1=s1,t2=s2;
	int j=0;
	for(int i=0; i<t1.size(); i++){
		if(t1[i]=='?'){
			t1[i]=(char)(s[j]+'0');
			j++;
		}
	}
	for(int i=0; i<t2.size(); i++){
		if(t2[i]=='?'){
			t2[i]=(char)(s[j]+'0');
			j++;
		}
	}
	int a1=atoi(t1);
	int a2=atoi(t2);
	int diff=abs(a2-a1);
	
	
	if(diff<mn){
		mn=diff;
		sc1=a1;
		sc2=a2;
		ans1=t1;
		ans2=t2;
	}
	else if(diff==mn){
		if(a1<sc1){
			sc1=a1;
			sc2=a2;
			ans1=t1;
			ans2=t2;
		}
		else if(a1==sc1 && a2<sc2){
			sc1=a1;
			sc2=a2;
			ans1=t1;
			ans2=t2;
		}
	}
}

void subsets(int i, int n){
	if(i==n){
		eval(n);
		return ;
	}
	for(int j=0; j<=9; j++){
		s[i]=j;
		subsets(i+1, n);
	}
}
int main(){
	iosbase;

	int t;
	cin>>t;

	for(int T=1; T<=t; T++){
		cin>>s1>>s2;
		int cnt=0;
		for(int i=0; i<s1.size(); i++){
			if(s1[i]=='?')cnt++;
		}
		for(int i=0; i<s2.size(); i++){
			if(s2[i]=='?')cnt++;
		}
		memset(s, 0, sizeof s);
		mn=intmax;
		sc1=intmax;
		sc2=intmax;
		subsets(0, cnt);
		cout<<"Case #"<<T<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}