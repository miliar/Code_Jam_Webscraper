#include <iostream>
#include <cstdio>
using namespace std;

long long solve(long long n){
	int dig[10] = {0}, cont = 10;
	long long i;
	for(i = 1; cont > 0; i++){
		long long k = i*n;
		do{
			if(dig[k%10LL] == 0){
				dig[k%10LL] = 1;
				cont--;
			}
			k /= 10LL;
		}while(k > 0);

	}
/*	if(i > 50)
        cout <<n<<" i = " <<i << endl;//*/
	return (i-1)*n;
}

int main(){
	int n, casos;
	cin >> casos;
	for(int i = 1; i <= casos; i++){
		cin >> n;
		if(n != 0){
            printf("Case #%d: %lld\n", i, solve(n));
		}
		else{
            printf("Case #%d: INSOMNIA\n", i);
		}
	}
	return 0;
}
