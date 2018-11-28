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
		freopen("out_1.txt", "r", stdin);
		//srand((int)time(NULL));
		forn(i, 50){
			string sc; ll cm[9], base[9];
			forn(z,9) { cm[z]=0; base[z]=1;}
			cin>>sc;
			for(int j=15; j>=0; j--) {
				forn(z, 9) {cm[z] += base[z]*(sc[j]-'0'); base[z]*=(z+2);}
			}
			vector<ll> pp(9);
			forn(j, 9) cin>>pp[j];
			forn(j, 9) if(cm[j]%pp[j]!=0) cout<<i<<endl; 
		}
		return 0;
	}
	
	freopen("D-small-attempt0.in", "r", stdin);//test.txt//B-small-attempt0.in
	freopen("out.txt", "w", stdout);

	int T; cin>>T;
	forn(i,T) {
		ll K,C,S; cin>>K>>C>>S;
		ll dis = 1;
		forn(j, C-1) dis*=K;
		cout<<"Case #"<<i+1<<":";
		forn(j,K) cout<<" "<< 1+dis*j;
		cout<<endl;
	}


	return 0;
}
