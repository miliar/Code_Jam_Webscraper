#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;

void gen(){
	freopen("testcase.txt", "w", stdout);
	exit(0);
}

vector<vector<int> > arr_g;
vector<int> pr_g, state;
bool fl;

void rec(int pos){
	int n = pr_g.size();
	if(pos == n)
		return;
	if(!fl)
		return;
	int ind = pr_g[pos];
	bool cur = false;
	for(int i=0; i<n; i++){
		if(arr_g[ind][i] == 1 && state[i] == 0){
			cur = true;
			state[i] = 1;
			rec(pos + 1);
			state[i] = 0;
		}
	}
	if(!cur){
		fl = false;
	}
}

bool check_2(vector<vector<int> > arr, vector<int> pr){
	fl = true;
	state.assign(pr.size(), 0);
	arr_g = arr;
	pr_g = pr;
	rec(0);
	return fl;
}

bool check(vector<vector<int> > arr){
	int n = arr.size();
	vector<int> pr(n);
	for(int i=0; i<n; i++){
		pr[i] = i;
	}
	do{
		if(!check_2(arr, pr)){
			return false;
		}
	}
	while(next_permutation(pr.begin(), pr.end()));

	return true;
}

int slow(int n, vector<vector<int> > arr){
	int res = 1e9;
	int cnt = 0;
	vector<int> index;
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			if(arr[i][j] == 0){
				cnt++;
				index.push_back(i*n + j);
			}
		}
	}

	vector<vector<int> > cur = arr;

	for(int i=0; i<(1<<cnt); i++){
		cur = arr;
		int cost = 0;

		for(int j=0; j<cnt; j++){
			if(i & (1 << j)){
				int ind = index[j];
				int ii = ind / n;
				int jj = ind % n;
				cur[ii][jj] = 1;
				cost++;
			}
		}
		if(check(cur)){
			res = min(res, cost);
		}
	}
	return res;
}

int main(){

#ifdef _CONSOLE
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("testcase.txt", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int countTest;
	cin>>countTest;	
	for(int test = 1; test <= countTest; test++){
		int n;
		cin>>n;
		vector<vector<int> > arr(n, vector<int> (n, 0));

		for(int i=0; i<n; i++){
			string str;
			cin>>str;
			for(int j=0; j<n; j++){
				if(str[j] == '1'){
					arr[i][j] = 1;
				}
			}
		}

		int res = slow(n, arr);

		printf("Case #%d: %d\n", test, res);
		cerr<<test<<"\n";
	}
	
	return 0;
}

