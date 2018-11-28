#include <bitset>
#include <iostream>
#include <fstream>

using namespace std;

void trocear(bitset<10> &digit, long long int &n);
int main(){
	ifstream ci("xxx.txt");
	ofstream cou("sol.txt");
	long long int casos, n, aux;
	ci >> casos;
	for (int i = 1; i <= casos; ++i){
		bitset<10> digit;
		digit.reset();
		ci >> n;
		if (n == 0){
			cou << "Case #" << i << ": INSOMNIA\n";
		}
		else{
			long int j = 1;
			while (!digit.all()){
				aux = n*j;
				trocear(digit, aux);
				++j;
			}
			cou << "Case #" << i << ": " << n*(j - 1) << "\n";
		}
	}
	return 0;
}
void trocear(bitset<10> &digit, long long int &n){
	while (n > 0){
		digit[n % 10] = true;
		n = n / 10;
	}
}