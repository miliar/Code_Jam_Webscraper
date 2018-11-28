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
	
	freopen("C-small-attempt0.in", "r", stdin);//test.txt//B-small-attempt0.in
	freopen("out_2.txt", "w", stdout);

	int T; cin>>T;
	forn(i,T) {
		ll N,J; cin>>N>>J;
		vector<ll> a1;
		set<ll> s1;
		a1.push_back(2);
		a1.push_back(3);
		s1.insert(2);
		s1.insert(3);

		for(int j=5; j<100000000; j+=2){//1000000
			//if(j%10000000 == 0) cout<<j/10000000<<endl;
			int f=1;
			for(int z=0; a1[z]*a1[z]<=j; z++) {
				if(j%a1[z]==0) {f=0;break;}
			}
			if(f) {a1.push_back(j); s1.insert(j);}
		}

		cout<<"Case #"<<i+1<<":"<<endl;
		int tf=0;
		//for(int j=33; j<64; j+=2){
		for(int j=32769; j<65536; j+=2){
			ll cm[9], base[9];
			forn(z,9) { cm[z]=0; base[z]=1;}
			int kj=j;
			stack<int> dn;
			while(kj>0) {
				int st = kj%2;
				forn(z, 9) {cm[z] += base[z]*st; base[z]*=(z+2);}
				kj/=2;
				dn.push(st);
			}

			int f=1;
			forn(z,9) if(s1.count(cm[z])) {f=0; break;}
			if(f && tf<J) {
				vector<ll> ds;
				forn(z,9) {
					ll p = cm[z];
					forn(b, a1.size()) if(p%a1[b]==0) { ds.push_back(a1[b]); break;}
				}
				if(ds.size()==9) {
					while(dn.size()) {cout<<dn.top();dn.pop();}
					forn(z,9) cout<<" "<<ds[z];
					cout<<endl;
					tf++;
				}
			}
			if(tf==J) break;
		}
	}


	return 0;
}
