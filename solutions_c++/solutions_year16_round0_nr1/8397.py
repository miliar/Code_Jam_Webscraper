#include <iostream>
using namespace std;

bool seen[10];
int count = 0;

void set_num(long long n){
	do{
		if(!seen[n%10]){
		seen[n%10]=true;
		count++;
		}
		n = n/10;
	}
	while(n > 0);
}

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int x = 0; x < t; x++){ 
		count = 0;
		for(int i=0; i<10; i++){
			seen[i] = false;
		}
		long long n;
		cin >> n;
		if(n == 0){
			cout << "Case #" << x+1 << ": INSOMNIA" << endl;
			continue;
		}
		long long j = 0;
		while(count != 10){
			j++;
			set_num(j*n);
		}
		cout << "Case #" << x+1 << ": " << j*n << endl;
	}
}