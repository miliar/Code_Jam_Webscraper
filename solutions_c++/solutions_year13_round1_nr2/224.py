#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <cctype>
#include <climits>
#include <cassert>
#include <sstream>
using namespace std;

#define MOD 1000000007

#define all(C) (C).begin(),(C).end()
#define tr(C, it) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); it++)

 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 

typedef long long LL;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;


struct ent {
	LL i;
	LL v;
};

bool compare(ent a, ent b) {
	return a.v >= b.v;
}

vector<LL> start(10000, 0);
vector<LL> finish(10000, 0);


LL process() {
	LL e,r,n, gain =0;
	cin>>e>>r>>n;
	vector<ent> a(n);
	vi mark(10000, 0);
	for (int i =0; i<n; i++) {
		cin>>a[i].v;
		a[i].i = i;
	}
	
	
	//b = a;
	stable_sort(a.begin(), a.end(), compare);
	//cout<<mark[0]<<"  debug"<<endl;
	LL pos, val, prev, next, energy, spendable;
	for (int i = 0; i<n; i++) {
		pos = a[i].i;
		val = a[i].v;
		mark[pos] = 1;
		prev = pos-1;
		while (prev >= 0 && !mark[prev]) prev--;
		//if (prev >= 0) cout<<" debug mark[prev]  = "<<mark[prev]<<endl;
		next = pos+1;
		while (next < n && !mark[next]) next++;
		//cout<<"i, pos, val, prev, next = "<<i<<' '<<pos<<' '<<val<<' '<<prev<<' '<<next<<endl;
		if (prev < 0) {
			energy = e;
		} else {
			energy =  min(e, finish[prev] + (pos - prev)*r);
		}
		
		if (next >= n) {
			spendable = energy;
		} else {
			if ((next - pos)*r >= start[next]) {
				spendable = energy;
			} else {
				spendable = max(0LL	, energy + (next - pos)*r - start[next]);
			}
		}
		
		start[pos] = energy;
		finish[pos] = energy - spendable;
		gain += spendable*val;
	}
	
	return gain;
}	

int main() {
  int i, t=1;
  cin >>t;
  for (i = 0; i <t; i++) {
    LL x = process();
	cout<<"Case #"<<i+1<<": "<<x<<endl;		
  }
}
