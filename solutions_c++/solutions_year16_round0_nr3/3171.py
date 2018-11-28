#include<bits/stdc++.h>

using namespace std;

int t, j, n;
vector<long long> L;

void GET(long long mask){
	long long num = 0, pot = 1;
	for(int i = n-1; i >= 0; i--){
		if(!i || i == n-1) if(!((1LL<<i)&mask)) return;
		if((1LL<<i)&mask) num += (pot);
		pot *= 10;
	}
	L.push_back(num);
}

long long get(long long num, long long base){
	int len = 0;
	long long ret = 0, pot = 1;
	while(num > 0){	
		int d = num % 10;
		num /= 10;
		ret += (d * pot);
		pot *= base;
		len++;
	}
	return ret;
}

long long D[15];
bool prime(long long num, long long base){
	for(long long k = 2; k*k <= num; k++) 
	 if(num % k == 0){
	  D[base] = k;
	  return false;
     }
	return true;
}

bool solve(long long num){
	for(int i = 2; i <= 10; i++){
		long long N = get(num,i);
		if(prime(N,i)) return false;
	} 
	return true;
}

int main(){
	
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	ofstream cout ("output.txt");
	
	cin >> t;
	int cases = 1;
	while(t--){
		cin >> n >> j;
		for(long long i = 0; i < (1LL<<n); i++) GET(i);
		int total = 0, pointer = 0;
		cout << "Case #" << cases++ << ":\n";
		while(total < j){
			if(solve(L[pointer])){
			 total++;
			 cout << L[pointer] << " ";
			 for(int i = 2; i <= 10; i++) cout << D[i] << " ";
			 cout << '\n';
			}
			pointer++;
		}
	}
	
	return 0;
	
}