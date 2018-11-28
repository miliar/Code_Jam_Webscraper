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
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;

bool check(string s){
	int i=0,j=s.size()-1;
	while(i<j){
		if(s[i]!=s[j])return false;
		i++;
		j--;
	}
	return true;
}

string intToString(int n){
	stringstream ss;
	ss<<n;
	return ss.str();
}

int main() {
	// freopen ("input.txt", "r", stdin);
	// freopen ("output.txt", "w", stdout);
	ll t,a,b;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>a>>b;
		int res=0;
		for(ll s=1,ss=1;ss<=b;s++,ss=s*s){
			if(a<=ss && ss<=b && check(intToString(ss)) && check(intToString(s))){
				res++;
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<res<<endl;
	}
}