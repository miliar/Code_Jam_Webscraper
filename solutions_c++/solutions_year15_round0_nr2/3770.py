#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<iterator>
using namespace std;


int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int n;
		cin >> n;
		vector<int> dish(n);
		for (int i = 0; i < n; i++){
			cin >> dish[i];
		}

		int ret = dish[0];
		for (int i = 1; i < n; i++){
			ret = max(ret, dish[i]);
		}

		for (int k = 2; k < ret; k++){
			int sum = k;
			for (int num : dish){
				sum += (num - 1) / k;
			}
			ret = min(ret, sum);
		}

		printf("Case #%d: %d\n", t, ret);
	}
	return 0;
}