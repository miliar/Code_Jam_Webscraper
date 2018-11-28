#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())


int main(){
	int run, runs;
	scanf("%d",&runs);
	for(run=1;run<=runs;run++){
		int n,i,j,k;
		int best=1000000;
		scanf("%d",&n);
		vi v(n);
		for(i=0;i<n;i++) scanf("%d",&v[i]);
		for(int h=1;h<=1000;h++){
			int cuts=0;
			for(i=0;i<n;i++){
				cuts+=(v[i]-1)/h;
			}
  		best=min(best,h+cuts);
		}


		printf("Case #%d: %d\n",run,best);
	}

}
