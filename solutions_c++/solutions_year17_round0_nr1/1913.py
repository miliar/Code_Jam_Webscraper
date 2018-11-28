#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(lli i=(lli)a;i<=(lli)b;i++)
#define endl "\n"
#define mp make_pair
#define X first
#define Y second
#define inf mod
#define mod 1000000007
#define pb push_back
#define pi 3.14159265359
#define gc getchar
#define Case cout<<"Case #"<<++cas<<": ";
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define all(v) v.begin(),v.end()
typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<lli,int> pli;
typedef vector<pii> vii;
typedef pair<lli,lli> pll;
typedef vector<lli> vl;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define pr(...) dbs(#__VA_ARGS__, __VA_ARGS__)
template <class T> void dbs(string str, T t) {cerr << str << " : " << t << "\n";}
template <class T, class... S> void dbs(string str, T t, S... s) {int idx = str.find(','); cerr << str.substr(0, idx) << " : " << t << ","; dbs(str.substr(idx + 1), s...);}
template <class S, class T>ostream& operator <<(ostream& os, const pair<S, T>& p) {return os << "(" << p.first << ", " << p.second << ")";}
template <class T>ostream& operator <<(ostream& os, const vector<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T>ostream& operator <<(ostream& os, const set<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class S, class T>ostream& operator <<(ostream& os, const map<S, T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T> void prc(T a, T b) {cerr << "["; for (T i = a; i != b; ++i) {if (i != a) cerr << ", "; cerr << *i;} cerr << "]\n";}

int main()
{
	fastio;
	lli T,n,k,cas=0;string s;
	cin>>T;
	while(T--)
	{
		bool flag=0;
		lli ans=0;
		cin>>s>>k;
		n=s.length();
		FOR(i,0,n-1)
		{
			if(s[i]=='-')
			{
				//pr(i);
				ans++;
				FOR(j,i,i+k-1)
				{if(j>=n) {flag=1;break;}
					if(s[j]=='-')
					s[j]='+';
				else s[j]='-';}
			}
		}
		Case;
		if(flag)
			cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
}