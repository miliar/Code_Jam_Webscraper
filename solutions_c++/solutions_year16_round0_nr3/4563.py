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

vector<vector<ll> > arr;

ll check_prime(ll numb){
	ll sq = sqrt((double)numb) + 100;
	for(ll i=2; i<sq; i++){
		if(i == numb){
			return -1;
		}
		if(numb % i == 0){
			return i;
		}
	}
	return -1;
}

pair<bool, vector<ll> > check(string cur){
	reverse(cur.begin(), cur.end());
	pair<bool, vector<ll> > res;
	res.first = true;


	for(int i=2; i<=10; i++){
		ll numb = 0;
		for(int j=0; j<cur.size(); j++){
			if(cur[j] == '1'){
				numb += arr[i][j];
			}
		}
		ll cur = check_prime(numb);
		if(cur == -1){
			res.first = false;
			break;
		}
		else{
			res.second.push_back(cur);
		}
	}

	return res;
}

int main(){

#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int count_test;
	cin>>count_test;

	arr.assign(11, vector<ll> (16));

	for(int i=2; i<=10; i++){
		ll cur = 1;
		ll buf = i;
		for(int j=0; j<arr[i].size(); j++){
			arr[i][j] = cur;
			cur *= buf;
		}
	}
	int state = 1;
	for(int test = 1; test <= count_test; test++){
		int n, k;
		cin>>k>>n;
		k -= 2;

		vector<pair<string, vector<ll> > > res;

		for(int i=0; i<(1<<k); i++){
			string cur;
			for(int j=0; j<k; j++){
				if(i & (1 << j)){
					cur += "1";
				}
				else{
					cur += "0";
				}
			}
			cur = "1" + cur + "1";
			

			pair<bool, vector<ll> > ch = check(cur);
			if(ch.first){
				res.push_back(make_pair(cur, ch.second));
			}

			if(res.size() == n){
				break;
			}
		}


		printf("Case #%d:\n", test);

		for(int i=0; i<n; i++){
			cout<<res[i].first<<" ";
			for(int j=0; j<res[i].second.size(); j++){
				cout<<res[i].second[j]<<" ";
			}
			cout<<"\n";
		}

	}


	
	return 0;
}

