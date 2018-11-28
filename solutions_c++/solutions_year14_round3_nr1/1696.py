#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <cassert>
#include <iomanip>
using namespace std;
static const double EPS = 1e-9;
static const int mod = 100000007;
typedef long long ll;

int t;
string str[101];

ll gcd(ll a,ll b){
	if(b==0)return a;
	return gcd(b,a%b);
}

vector<string> split(const string &str, const string &delim){
  vector<string> res;
  size_t current = 0, found, delimlen = delim.size();
  while((found = str.find(delim, current)) != string::npos){
    res.push_back(string(str, current, found - current));
    current = found + delimlen;
  }
  res.push_back(string(str, current, str.size() - current));
  return res;
}

int main() {
	// freopen ("input.txt", "r", stdin);
	// freopen ("output.txt", "w", stdout);
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<(i+1)<<": ";
		string str;
		cin>>str;
		vector<string> strs=split(str,"/");
		ll a=atoi(strs[0].c_str()),b=atoi(strs[1].c_str()),c=gcd(b,a);
		a/=c;
		b/=c;
		
		ll x=1;
		bool ok=false;
		while(x<=b){
			if(x==b)ok=true;
			x<<=1;
		}
		if(!ok){
			cout<<"impossible"<<endl;
			continue;
		}

		int res=0;
		while(a<b){
			res++;
			a<<=1;
		}
		cout<<res<<endl;
	}
}