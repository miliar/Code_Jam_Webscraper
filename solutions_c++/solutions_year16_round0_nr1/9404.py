#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
#define vi vector<int> 
#define rep(i, n) for(int i=0; i<n; i++)
bool allDone(vi &v, long long no){
	while(no>0){
		v[no%10]++;
		no/=10;
	}
	rep(i, v.size()){
		if(v[i]== 0){
			return false;	
		}
	}
	return true;
}
void solve(){
	long long no;
	cin >> no;
	vi v(10, 0);
	long long temp=no;
	long long i=2;
	if(no==0){
		cout << "INSOMNIA" <<endl;
	}
	else{
		while(!allDone(v, no)){
			no = i*temp;
			i++;
		}
		cout << no << endl;
	}
}
main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	rep(i, t){
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
	
}
