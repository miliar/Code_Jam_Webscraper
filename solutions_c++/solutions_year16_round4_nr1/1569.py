#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

inline int winner(int a, int b){
	if(a>b) swap(a, b);
	if(a==1 && b==2) return 1;
	if(a==1 && b==3) return 3;
	if(a==2 && b==3) return 2;
	assert(false);
	return -1;
}

bool ok(const vector<int>& pp){
	int n = pp.size();
	vector< vector<int> > f(2);
	f[0].reserve(n);
	f[1].reserve(n);
	for(int i=0; i<n; i+=2){
		assert(i+1<n);
		if(pp[i]==pp[i+1]) return false;
		f[0].push_back(winner(pp[i],pp[i+1]));
	}
	int cur = 0, next = 1;
	while(f[cur].size()>1){
		f[next].clear();
		for(int i=0; i<f[cur].size(); i+=2){
			assert(i+1<f[cur].size());
			int u = f[cur][i];
			int v = f[cur][i+1];
			if(u==v) return false;
			f[next].push_back(winner(u, v));
		}
		cur = 1-cur;
		next = 1-next;
	}
	return true;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int n, r, p, s;
		cin>>n>>r>>p>>s;
		int total = (1<<n);
		vector<int> pp;
		pp.reserve(total);
		for(int i=0; i<p; i++) pp.push_back(1);
		for(int i=0; i<r; i++) pp.push_back(2);
		for(int i=0; i<s; i++) pp.push_back(3);
		assert(pp.size()==total);
		bool done = false;
		do {
			if(ok(pp)){
				cout<<"Case #"<<testnum+1<<": ";
				for(int i=0; i<total; i++){
					switch(pp[i]){
					case 1:
						cout<<'P';
						break;
					case 2:
						cout<<'R';
						break;
					case 3:
						cout<<'S';
						break;
					}
				}
				cout<<endl;
				done = true;
			}
		} while (!done && next_permutation(pp.begin(), pp.end()));
		if(!done){
			cout<<"Case #"<<testnum+1<<": IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
