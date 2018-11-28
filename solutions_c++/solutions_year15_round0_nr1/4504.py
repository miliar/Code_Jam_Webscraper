#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <numeric>
#include <ratio>
#include <regex>
#include <string>
#include <tuple>
#include <utility>
#include <valarray>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS
#define INF ULLONG_MAX
#define MIN LLONG_MIN
#define pi 3.1415926535897932384626433832795

#define sz(v) v.size()
#define pb(x) push_back(x)
#define re return
#define sum(v) accumulate(v.begin(),v.end(),0)
#define asrt(v) sort(v.begin(),v.end())
#define dsrt(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define str to_string
#define print(v) for (auto& i:v) cout<<i<<endl
#define print "Case #"+to_string(t1)+": " 

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;

int main() {
	freopen("Data/A.txt", "r", stdin);
	freopen("Data/A1.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1; t1<=T; t1++) {
		int s;
		cin>>s;
		string ss;
		cin>>ss;
		int added=0,total=ss[0]-'0';
		for(int i=1; i<=s; i++) {
			if(total>=i) {
				total+=ss[i]-'0';
			} else{
				if(ss[i]!='0') {
					added+=i-total;
					total+=i+ss[i]-'0';
				}
			}
		}
		cout<<print<<added<<endl;
	}
	getchar();
	return 0;
}
