#include <cstdio>
#include <math.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <queue>
#include <cstring>
#include <iomanip>
#include <deque>
#include <stack>
#include <map>
#include <set>

#define forn(i,n) for(int i=0;i<n;i++)

using namespace std;

typedef long long ll;

typedef unsigned long long ull;

typedef pair<int, int> P2;
typedef pair<ll, ll> P2l;

#define INF 1000000

int main()
{
	int debug = 0;
	if(debug){
		//freopen("out_1.txt", "r", stdin);
		//srand((int)time(NULL));
		return 0;
	}
	
	freopen("A-large.in", "r", stdin);//test.txt
	freopen("A-large.txt", "w", stdout);

	int T; cin>>T;
	forn(i,T) {
		string s,t; cin>>s;
		t = s[0];
		for(int j=1;j<s.size();j++) if(s[j]>=t[0]) t = s[j]+t; else t = t+s[j]; 
		cout<<"Case #"<<i+1<<": "<<t<<endl;
	}

	return 0;
}
