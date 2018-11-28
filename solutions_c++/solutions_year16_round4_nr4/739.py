#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <assert.h>
using namespace std;
int n;
int a[5][5];
int ans;
int ree(vector<int> & p, int i, int msk){
	if(i == n)return 1;
	bool f = 1;
	bool t = 0;
	for(int j = 0; j < n; j++){
		if(a[p[i]][j] && (msk & (1 << j)) == 0){
			t = 1;
			f &= ree(p, i + 1, msk | (1 << j));
		}
	}
	if(t == 0)
		return 0;
	return f;
}
bool check(){
	vector<int> p;
	for(int i = 0; i < n; i++)
		p.push_back(i);
	bool f = 1;
	do{
		f &= ree(p, 0, 0);
	}while(next_permutation(p.begin(), p.end()));
	
	if(f && ! ree(p, 0, 0))assert(false);
	return f;
}
void re(int i, int j, int cst){
	if(i == n){
		if(check()){
			/*
			if(cst == 2){
				cout << endl;
				for(int i = 0; i < n; i++){
					for(int j = 0; j < n; j++){
						cout << a[i][j];
					}
					cout << endl;
				}
				cout << endl;
				}*/
			ans = min(ans, cst);
		}
		return;
	}
	if(j == n){
		re(i + 1, 0, cst);
		return;
	}
	if(a[i][j] == 1)re(i, j + 1, cst);
	else{
		re(i, j + 1, cst);
		a[i][j] = 1;
		re(i, j + 1, cst + 1);
		a[i][j] = 0;
	}
}
void solve(){
	cin >> n;
	char ch;
	for(int i = 0; i < n; i++){
		for(int j  = 0; j < n; j++){
			cin >> ch;
			a[i][j] = ch - '0';
		}
	}
	
	ans = n * n + 5;
	re(0, 0, 0);
	cout << ans << endl;
}
int main(){
	int t;
	cin >> t;
	for(int i = 0; i <t; i++){
		printf("Case #%d: ", i + 1);	solve();
	}
	return 0;
}
