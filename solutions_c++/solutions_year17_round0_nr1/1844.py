#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int, int> mii;
typedef map<string, int> msi;

#define zero(arr) memset((arr), 0, sizeof (arr))
#define init(arr) memset((arr), -1, sizeof (arr))

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t, k;
	string s;
	
	
	cin>>t;
	
	
	for(int cs = 1; cs <= t; cs++) {
		
		cin>>s;
		cin>>k;
		
		bool can = 1;
		int cnt = 0;
		
		for(int i = 0; i < s.length(); i++) {
			if(s[i] == '-') {
				if(s.length() - i >= k) {
					for(int j = i; j < i + k; j++) {
						if(s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
					}
					cnt++;
				} else {
					if(s[i] == '-')
						can = 0;
				}
			}
		}
		cout<<"Case #"<<cs<<": ";
		
		if(can)
			cout<<cnt;
		else
			cout<<"IMPOSSIBLE";
		cout<<'\n';
	}
		
	return 0;
}

