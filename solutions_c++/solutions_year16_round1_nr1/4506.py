#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <memory>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

#define rep(i,b,e) for(int i=b;i<e;++i)
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

static const ll Zp = 1000000009;
static const double EPS = 1e-9;

int T;

vector<string> rec(string b, string s)
{
	vector<string> ss;
	if (s.empty()) {
		ss.pb(b);
		return ss;
	}

	ss = rec( string(b).append(1, s[0]), string(s.begin()+1, s.end()));

	vector<string> ss2;
	ss2 = rec( string(1,s[0]).append(b), string(s.begin()+1, s.end()));

	std::copy(ss2.begin(), ss2.end(), back_inserter(ss));

	return ss;
}

string solve(string s){
	vector<string> ss;

	ss = rec("", s);

	sort(ss.begin(), ss.end());

    return ss[ss.size()-1];
}

int main() {
    cin>>T;
    for(int t=1;t<=T;++t) {
    	string s;
    	cin >> s;
        cout<<"Case #"<<t<<": "<<solve(s)<<endl;
    }
    return 0;
}
