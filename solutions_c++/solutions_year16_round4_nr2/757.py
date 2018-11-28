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

double get(vector<double> cur){
	double res = 0;
	int n = cur.size();
	for(int i=0; i<(1 << n); i++){
		int cnt = 0;
		for(int j=0; j<n; j++){
			if(i & (1 << j)){
				cnt++;
			}
		}

		if(cnt * 2 == n){
			double p = 1;
			for(int j=0; j<n; j++){
				if(i & (1 << j)){
					p *= cur[j];
				}
				else{
					p *= (1.0 - cur[j]);
				}
			}
			res += p;
		}

	}
	return res;
}

double slow(int n, int k, vector<double> arr){
	double res = 0;
	vector<double> cur;
	for(int i=0; i<(1<<n); i++){
		int cnt = 0;
		for(int j=0; j<n; j++){
			if(i & (1 << j)){
				cnt++;
			}
		}
		if(cnt == k){
			cur.clear();
			for(int j=0; j<n; j++){
				if(i & (1 << j)){
					cur.push_back(arr[j]);
				}
			}
			double p = get(cur);
			res = max(res, p);
		}
	}

	return res;
}

int main(){

#ifdef _CONSOLE
	freopen("B-small-attempt0.in", "r", stdin);
	//freopen("testcase.txt", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int countTest;
	cin>>countTest;	
	for(int test = 1; test <= countTest; test++){
		int n, k;
		cin>>n>>k;
		vector<double> arr(n);

		for(int i=0; i<n; i++){
			cin>>arr[i];
		}

		double res = slow(n, k, arr);

		printf("Case #%d: ", test);
		cout<<res<<"\n";
		cerr<<test<<"\n";
	}
	
	return 0;
}

