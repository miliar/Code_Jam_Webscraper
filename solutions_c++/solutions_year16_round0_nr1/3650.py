#include<bits/stdc++.h>

using namespace std;

int t;
long long n;
bool digit[10];

bool ok(){
	for(int i = 0; i <= 9; i++)
	 if(!digit[i]) return false;
	return true;
}

void solve(long long num){
	while(num > 0){
		int d = num % 10;
		digit[d] = true;
		num /= 10;
	}
}

int main(){
	
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	
	cin >> t;
	int cases = 1;
	while(t--){
		cin >> n;
		if(!n){
			cout << "Case #" << cases++ << ": " << "INSOMNIA" << '\n';
			continue; 
		}
		for(int i = 0; i <= 9; i++) digit[i] = false;
		long long cont = 1;
		while(1){
		 solve(cont*n);
		 if(ok()) break;
		 cont++;
	    }
		cout << "Case #" << cases++ << ": " << cont*n << '\n';
	}
	
	return 0;
	
}