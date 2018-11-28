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

int t,n;
string L;

char buf[]={'a','e','i','o','u'};
bool check(string str){
	int a=0;
	for(int i=0;i<str.size();i++){
		bool f=true;
		for(int j=0;j<5;j++){
			if(buf[j]==str[i]){
				f=false;
			}
		}
		if(f)a++;
		else a=0;
		if(n<=a)return true;
	}
	return false;
}

void solve(){
	cin>>L>>n;
	int ans=0;
	for(int i=0;i<L.size();i++){
		for(int j=i+1;j<=L.size();j++){
			if(check(L.substr(i,j-i)))ans++;
		}
	}
	cout<<ans<<endl;
}

int main() {
	// freopen ("input.txt", "r", stdin);
	// freopen ("output.txt", "w", stdout);

	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<(i+1)<<": ";
		solve();
	}
}