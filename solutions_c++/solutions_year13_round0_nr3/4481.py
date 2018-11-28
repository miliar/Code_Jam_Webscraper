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
	int t;
	cin>>t;
	int cnt=1;
	VI sq(1001,0);
	rep(i,33){
		int ii=i*i;
		stringstream n1;n1<<i;
		stringstream n2;n2<<ii;
		string s1,s2,s3,s4;
		n1>>s1;n2>>s3;
		s2=s1;s4=s3;
		reverse(full(s2));
		reverse(full(s4));
		if(s1==s2 && s3==s4)
			sq[ii]=1;
	}
	while(t--){
		int a,b;
		cin>>a>>b;
		int x=0;
		repx(i,a,b+1)
			if(sq[i])
				x++;
		cout<<"Case #"<<cnt++<<": "<<x<<endl;		
	}
	return 0;
}
