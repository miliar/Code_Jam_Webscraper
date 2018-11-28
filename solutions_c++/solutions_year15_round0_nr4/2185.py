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
	freopen("Data/C.txt", "r", stdin);
	freopen("Data/C1.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t1=1; t1<=T; t1++) {
		int x,r,c;
		cin>>x>>r>>c;
		cout<<print;
		if(x==1) cout<<"GABRIEL"<<endl;
		else if(x==2) {
			if(r*c%2==0) cout<<"GABRIEL"<<endl;
			else cout<<"RICHARD"<<endl;
		}
		else if(x==3) {
			if(r*c%3!=0 || r==1 || c==1) cout<<"RICHARD"<<endl;
			else cout<<"GABRIEL"<<endl;
		} else if(x==4) {
			if(r*c%4!=0 || r==1 || c==1 || r==2 || c==2) cout<<"RICHARD"<<endl;
			else cout<<"GABRIEL"<<endl;
		}
	}
	getchar();
	return 0;
}
