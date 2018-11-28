#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <queue>
#include <cstring>

#define pb push_back
#define VI vector<int>
#define VS vector<string>
#define sz(v) v.size()
#define len(s) s.length()
#define full(v) v.begin(),v.end()

#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)

typedef long long ll;

const int INF = 1<<30;

using namespace std;

int main(void){
	ll r,t,cas;
	cin>>cas;
	int x=1;
	while(cas--){
		cin>>r>>t;
		r++;
		int f=1,cnt=0;
		while(f){
			t-=(r*r-(r-1)*(r-1));
			if(t>=0)	cnt++;
			else f=0;
			r+=2;
		}
		cout<<"Case #"<<x++<<": ";
		cout<<cnt<<endl;
	}
	return 0;
}
