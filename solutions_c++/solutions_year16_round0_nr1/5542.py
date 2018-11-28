#include <stdio.h>
#include <iostream>
#include <set>
using namespace std;
set<int> s;
void add(int x){
	while(x){
		s.insert(x % 10);
		x /= 10;
	}
}
int mx = 0;
void solve(int n){
	s.clear();
	if(n == 0){
		cout <<"INSOMNIA";
		return;
	}
	int j;
	for(j = 1; s.size() < 10; j++){
		add(j * n);
	}
	j--;
	mx = max(mx, j);
	//if(j == 72) cout << n << endl;
	cout << j * n;
}
int main(){
	/*	for(int i = 1; i < 10000001; i++){
		solve(i);
	}
	cout << mx << endl;
	return 0;*/
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int n;
		cin >> n;
		cout << "Case #" << i + 1 << ": ";
		solve(n);
		cout << endl;
	}
	return 0;
}
