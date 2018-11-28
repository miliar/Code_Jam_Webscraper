#include <iostream>
using namespace std;

int counter;
bool tab[10];

bool test(unsigned long long n){
	while(n){
		if(tab[n%10] == false){
			counter++;
			tab[n%10] = true;
		}
		n/=10;
	}
	return counter == 10;
}

int main(){
	int t,n;
	cin >> t;
	for(int I=0; I<t; I++){
		counter = 0;
		for(int i=0; i<10; i++)tab[i] = false;
		cin >> n;
		if(n==0) {
			cout << "Case #" << I+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		unsigned long long N = n;
		while(!test(N)){
			N+=n;
		}
		cout << "Case #" << I+1 << ": " << N << endl;
	}
}
