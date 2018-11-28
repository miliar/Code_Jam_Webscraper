#include <iostream>
#include <vector>

using namespace std;

typedef int num;

void add(num n, vector<bool> &numbers){
	num rest = n;
	while(rest>0){
		numbers[rest%10] = true;
		rest = rest/10;
	}
}

bool All(vector<bool> &numbers){
	for(int i=0; i<=9; i++){
		if(!numbers[i]){
			return false;
		}
	}
	return true;
}

num solve(int n){
	num auxN = n;
	vector<bool> numbers(10);
	add(auxN, numbers);
	while(!All(numbers)){
		auxN+=n;
		add(auxN, numbers);
	}
	return auxN;
}

int main(){
	int T;
	cin >> T;
	vector<int> cases(T);
	for(int i=0; i<T; i++){
		cin >> cases[i];
	}

	for(int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": ";
		if(cases[i]==0){
			cout << "INSOMNIA";
		}else{
			cout << solve(cases[i]);
		}
		cout << endl;
	}

	return 0;
}