#include <iostream>
#include <stack>
#include <cmath>
using namespace std;

long long int have_divisor[(1 << 17) + 1][11];

long long int divisor(long long int i, long long int pods){
	long long int z = i;
	long long int mnoznik = 1;
	long long int wynik = 0;
	while(z > 0){
		wynik = wynik + (z % 2) * mnoznik;
		z = z / 2;
		mnoznik = mnoznik * pods;
	}
	
	for(long long int i = 2; i <= sqrt(wynik) + 1; i++){
		if(wynik % i == 0)
			return i;
	}
	
	return -1;
}

int main(){
	long long int T;
	T = 1;
	
	for(long long int z = 1; z <= T; z++){
		
		cout << "Case #" << z << ": " << endl;
		
		long long int zz = 0;
		for(long long int i = (1 << 15); i < (1 << 16); i++){
			for(long long int j = 2; j <= 10; j++){
				have_divisor[i][j] = divisor(i, j);
			}
			
			long long int ma = 0;
			for(long long int j = 2; j <= 10; j++){
				if(have_divisor[i][j] != -1)
					ma++;
			}
			if(ma == 9){
				long long int l = i;
				stack <char> stos;
				while(l > 0)
				{
					stos.push((l % 2) + '0');
					l = l / 2;
				}
				string H = "";
				while(!stos.empty()){
					H = H + (char)stos.top();
					stos.pop();
				}
				if(H[0] == '1' && H[H.size() - 1] == '1'){
					zz++;
					cout << H;
					for(long long int j = 2; j <= 10; j++){
						cout << " " << have_divisor[i][j];
					}
					cout << endl;
				}
			}
			
			if(zz == 50)
				return 0;
		}
	}	
	return 0;
}
