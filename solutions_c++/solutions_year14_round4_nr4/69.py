#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<string> vs;

int m;
vs data;
int n;
vector<int> state;
int best;
int countBest;
vector<vs> check;

void calc(int x);

int main() {
	int cases;
	scanf("%d",&cases);
	for(int round=1; round<=cases; round++) {
		scanf("%d%d",&m,&n);
		data.resize(m);
		for(int i=0; i<m; i++)
			cin>>ws>>data[i];
		state.resize(m);
		best=0;
		countBest=0;
		calc(0);
		printf("Case #%d: %d %d\n",round,best,countBest);
	}
	return 0;
}

void calc(int x) {
	if(x==m) {
		check.assign(n,vs());
		for(int i=0; i<m; i++) {
			int pos=state[i];
			for(int j=0; j<=(int)data[i].size(); j++)
				check[pos].push_back(data[i].substr(0,j));
		}
		for(int i=0; i<n; i++)
			if(check[i].empty())
				return;
		int curr=0;
		for(int i=0; i<n; i++) {
			sort(check[i].begin(),check[i].end());
			check[i].erase(unique(check[i].begin(),check[i].end()),check[i].end());
			curr+=check[i].size();
		}
		if(curr==best) {
			countBest++;
		} else if(curr>best) {
			best=curr;
			countBest=1;
		}
	} else {
		for(int i=0; i<n; i++) {
			state[x]=i;
			calc(x+1);
		}
	}
}

