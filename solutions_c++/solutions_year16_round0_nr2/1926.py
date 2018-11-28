/*
        By: facug91
        From: 
        Name: 
        Date: 09/04/2016
*/

#include <bits/stdc++.h>
#define endl "\n"
#define EPS 1e-9
#define MP make_pair
#define F first
#define S second
#define DB(x) cerr << " #" << (#x) << ": " << (x)
#define DBL(x) cerr << " #" << (#x) << ": " << (x) << endl
const double PI = acos(-1.0);

#define INF 1000000000
//#define MOD 1000000007ll
//#define MAXN 1000005

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> ii; typedef pair<ii, ii> iiii;
typedef vector<int> vi; typedef vector<ii> vii; typedef vector<iiii> viiii;

string s;

bool hasNegative () {
	for (char c : s) if (c == '-') return true;
	return false;
}

int main () {
	#ifdef ONLINE_JUDGE
		ios_base::sync_with_stdio(0); cin.tie(0);
	#endif
	//cout<<fixed<<setprecision(3); //cerr<<fixed<<setprecision(3); //cin.ignore(INT_MAX, ' '); //cout << setfill('0') << setw(5)
	int tc = 1;
	
	cin>>tc;
	for (int it=1; it<=tc; it++) {
		cin>>s;
		int l, ans = 0;
		while (hasNegative()) {
			if (s[0] == '-') {
				l = s.length()-1;
				while (s[l] != '-') l--;
				l++;
			} else {
				l = 0;
				while (l < s.length() && s[l] == '+') l++;
			}
			reverse(s.begin(), s.begin()+l);
			for (int i=0; i<l; i++) s[i] = ((s[i] == '-') ? '+' : '-');
			ans++;
		}
		cout<<"Case #"<<it<<": "<<ans<<endl;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
