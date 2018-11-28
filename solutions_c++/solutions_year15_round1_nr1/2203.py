#include <iostream>
#include <string>
#include <sstream>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <list>
#include <bitset>
#include <numeric>
using namespace std;

#define ll long long
#define ull unsigned long long
#define INF 1e9
#define MOD 1000000007
#define getcx getchar_unlocked
#define putcx putchar_unlocked
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64

ll m1(vector<ll>& m){
	ll res = 0;
	for(int i=1;i<m.size();i++){
		res = res + max(m[i-1] - m[i],(ll)0);
	}
	return res;
}

ll m2(vector<ll>& m){
	double rate = 0;
	for(int i=1;i<m.size();i++){
		rate = max(rate, (m[i-1]-m[i])/10.0);
	}
	ll res = 0;
	for(int i=0;i<m.size()-1;i++){
		res = res + min((ll)(10*rate), m[i]);
	}
	return res;
}


int main(){
	ios_base::sync_with_stdio(0);
	
	int T,n;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>n;
		vector<ll> m(n);
		for(int i=0;i<n;i++) cin>>m[i];
		cout<<"Case #"<<t<<": "<<m1(m)<<" "<<m2(m)<<endl;
	}

	return 0;
}