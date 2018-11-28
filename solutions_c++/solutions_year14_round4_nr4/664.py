#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
const int MAX = 10;

int n, numServer;
string data[MAX];

void input(){
	scanf("%d%d", &n, &numServer);
	
	int i;
	for(i = 0; i<n; i++)
		cin >> data[i];
}

int pos[MAX];
vector < string > server[MAX];

int count(vector < string > &target, int s, int e, int pos){
	if(s == e)
		return target[s].size()-pos;

	int i, ret = 0, prev = s;
	for(i = s+1; i<=e; i++){
		if(target[i-1].size() > pos){
			if(target[i-1][pos] != target[i][pos]){
				ret++;
				ret += count(target, prev, i-1, pos+1);
				prev = i;
			}
		} else if(target[i].size() > pos)
			prev = i;
	}
	ret++;
	ret += count(target, prev, e, pos+1);

	return ret;
}

void solve(){
	int i, res = 0, rCount = 0;
	for(i = 0; i<=n; i++)
		pos[i] = 0;

	while(pos[n] == 0){
		for(i = 0; i<n; i++)
			server[i].clear();

		for(i = 0; i<n; i++)
			server[pos[i]].push_back(data[i]);

		for(i = 0; i<numServer; i++)
			sort(server[i].begin(), server[i].end());

		int t = 0;
		for(i = 0; i<numServer; i++){
			if(!server[i].empty())
				t += count(server[i], 0, server[i].size()-1, 0)+1;
		}

		if(res < t){
			res = t;
			rCount = 1;
		} else if(res == t)
			rCount++;

		pos[0]++;
		for(i = 0; pos[i]>=numServer && i<n; i++){
			pos[i] -= numServer;
			pos[i+1]++;
		}
	}

	printf("%d %d\n", res, rCount);
}

int main(){
	freopen("output.txt", "w", stdout);

	int numCase, t;
	scanf("%d", &numCase);
	for(t = 1; t <= numCase; t++){
		printf("Case #%d: ", t);

		input();
		solve();
	}

	return 0;
}