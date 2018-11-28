using namespace std;
#include <iostream>
#include <string>

int t, vet[1010], res, n, num;
string str;

int main(){

	cin >> t;
	for(int cont = 1;cont <= t;cont++){
		res = 0;
		num = 0;		
		cin >> n;
		
		for(int i = 0;i <= n;i++){
			char x;
			cin >> x;
			vet[i] = x-'0';
		}

		for(int i = 0;i <= n;i++){
			if(num < i){
				res += i-num;
				num = i;
			}
			num += vet[i];
		}

		cout << "Case #" << cont << ": " << res << endl;
	}

	return 0;
}
