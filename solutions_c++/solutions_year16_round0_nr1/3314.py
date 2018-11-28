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

ll chk(ll in, ll st){
	while(in>0) {
		st |= (1<<(in%10));
		in/=10;
	}
	return st;
}


int main()
{
	int debug = 0;
	if(debug){
		freopen("test.txt", "w", stdout);
		srand((int)time(NULL));
		return 0;
	}
	
	freopen("A-large.in", "r", stdin);//test.txt
	freopen("A-large.txt", "w", stdout);

	int T; cin>>T;
	forn(i,T) {
		ll N; cin>>N;
		if(!N) cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else {
			ll state=0;
			forn(j, 100000) {
				state = chk(N*(j+1), state);
				if(state==1023) { cout<<"Case #"<<i+1<<": "<<N*(j+1)<<endl; break;}
			}
			if(state!=1023) cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
	}


	return 0;
}
