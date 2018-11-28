#include <iostream>

using namespace std;

bool chk(long long int n){
	int m;
	long long int rev = 0, chk;
	
	chk = n;
	while(n > 0){
		m = n % 10;
		rev = rev * 10 + m;
		n = n / 10;
	}
	if(rev == chk){
		return true;
	}
	else 
		return false;
}

int main(){
	long long int a, b, mem[100] = {0}, k, count = 0, i ,t, n = 1;

	for(i = 1; i <= 10000000; i++){
		if(chk(i)){
			k = i * i;
			if(chk(k)){
				mem[count] = k;
				count++;
			}
		}
	}

	cin >> t;
	while(t--){
		k = 0;
		cin >> a >> b;
		for(i = 0; i < count; i++){
			if(mem[i] >= a && mem[i] <= b)
				k++;
		}
		cout << "Case #" << n << ": " << k << endl;
		n++;
	}
	return 0;
}
	
