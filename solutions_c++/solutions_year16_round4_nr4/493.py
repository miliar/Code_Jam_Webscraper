#include "bits/stdc++.h"
using namespace std;
const int N = 30;
int t;
int n;
char arr[N][N];
int ans;
int solve(int mask1 , int mask2){
	int mn = N;
	for(int i = 0 ; i < n ; ++i){
		if(!(mask1 & (1 << i))){
			for(int j = 0 ; j < n ; ++j){
				if(!(mask2 & (1 << j))){
					if(arr[i][j] == '1'){
						mn = min(mn , 1 + solve(mask1 | (1 << i) , mask2 | (1 << j)));
					}
				}
			}
		}
	}
	if(mn == N){
		mn = 0;
	}
	return mn;
}
bool check(){
	return solve(0 , 0) == n;
}
int main(){
	cin >> t;
	for(int tc = 1 ; tc <= t ; ++tc){
		cout << "Case #" << tc << ": ";
		cin >> n;
		for(int i = 0 ; i < n ; ++i){
			cin >> arr[i];
		}
		vector < pair < int , int > > v;
		v.clear();
		for(int i = 0 ; i < n ; ++i){
			for(int j = 0 ; j < n ; ++j){
				if(arr[i][j] == '0'){
					v.emplace_back(make_pair(i , j));
				}
			}
		}
		ans = int(v.size());
		int p = 1 << (int(v.size()));
		for(int i = 0 ; i < p ; ++i){
			if(__builtin_popcount(i) >= ans){
				continue;
			}
			for(int j = 0 ; j < v.size() ; ++j){
				if(i & (1 << j)){
					arr[v[j].first][v[j].second] = '1';
				}
			}
			if(check()){
				ans = min(ans , __builtin_popcount(i));
			}
			for(int j = 0 ; j < v.size() ; ++j){
				if(i & (1 << j)){
					arr[v[j].first][v[j].second] = '0';
				}
			}
		}
		cout << ans << endl;
	}
}