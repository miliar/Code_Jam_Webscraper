#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void marcar_digitos(vector<bool>& digitos,long long x){
	int a;
	while (x != 0){
		a = x % 10;
		digitos[a] = true;
		x = x/10;
	}	
}

int main(){
	long long n,x;
	int t;
	cin >> t;
	
	for (int i = 1; i<=t; i++){
		vector<bool> digitos (10,false);
		cin >> n;
		
		if (n == 0){
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}
		
		int j = 1;
		while (count(digitos.begin(),digitos.end(),true) < 10){
			x=n*j;
			marcar_digitos(digitos,x);
			j++;
		}
		cout << "Case #" << i << ": " << x << endl;
	}
	
	return 0;
}
