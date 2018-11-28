#include <iostream>

using namespace std;

int N, T;

bool allfound(bool digits[]){
	for(int i = 0; i < 10; ++i){
		if(!digits[i])
			return false;
	}
	return true;
}

long long howmany(){
	bool digits[10] = {0};
	long long i = 1, res, aux;
	while(!allfound(digits)){
		res = (i++) * N;
		aux = res;
		while(aux > 0){
			long long div = (aux/10)*10;
			long long digit = aux - div;
			digits[digit] = true;
			aux /= 10;
		}
	}
	return res;
}

int main(){
	cin >> T;
	for(int i = 1; i <= T; ++i){
		cin >> N;
		cout << "Case #" << i << ": ";
		if(N == 0){
			cout << "INSOMNIA" << endl;
		}else{
			cout << howmany() << endl;
		}
	}
}

