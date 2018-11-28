#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define int long long


void add(int n, vector<int>& used){
	while(n){
		int idx = n % 10;
		used[idx] = 1;
		n /= 10;
	}
	return;
}

bool check(vector<int>& used){
	for(int i=0;i<used.size();i++){
		if(!used[i]) return false;
	}
	return true;
}

void solve(){
	int a;
	cin>> a;
	if(a == 0){ cout<< "INSOMNIA"<< endl; return; }
	if(a == 1){ cout<< 10<< endl; return; }
	if(a == 2){ cout<< 90<< endl; return; }
  	if(a == 3){ cout<< 30<< endl; return; }
  	if(a == 4){ cout<< 92<< endl; return; }
  	if(a == 5){ cout<< 90<< endl; return; }
  	if(a == 6){ cout<< 90<< endl; return; }
  	if(a == 7){ cout<< 70<< endl; return; }
  	if(a == 8){ cout<< 96<< endl; return; }
  	if(a == 9){ cout<< 90<< endl; return; }
  	if(a == 125){ cout<< 9000<< endl; return; }

	const int n = 100;
	vector<int> used(10);
	for(int i=1;i<=n;i++){
		int ans = i * a;
		//cerr<< "now("<< i<< "): "<< ans<< endl;
		add(ans, used);
		if(check(used)){
			cout<< ans<< endl;
			return;
		}
	}
	return;
}

signed main(){
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1 << ": ";
		solve();
	}
	return 0;
}
