#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

bool check(int *array){
	int i;
	//cout << "\n\n" << "Starting procedure to check array." << endl;
	for(i = 0; i < 10; i++){
		//cout << array[i] << " ";
		if(array[i] != 1) return false;
	}
	//cout << endl;
	return true;
}

void countSheep(long long int n){
	int size, i, d, k = 1;
	long long int sheep;
	int array[10];
	string s;
	if(n == 0){
		cout << "INSOMNIA" << endl;
		return;
	}
	//cout << "Starting procedure to count sheep" << endl;
	for(i = 0; i < 10; i++) array[i] = 0;
	while(1){
		sheep = n*k;
		//cout << "We are on sheep number: " << sheep << endl;
		s = to_string(sheep);
		size = s.size();
		for(i = size - 1; i >= 0; i--){
			d = atoi(&s[i]);
			//cout << "Digit that was checked: " << d << endl;
			array[d] = 1;
			s[i] = '\0';
		}
		if(check(array)){
			cout << sheep << endl;
			return;
		}
		k++;
	}
}

int main(int argc, char *argv[]){
	long long int ncases, n;
	int i;
	cin >> ncases;
	for(i = 1; i <= ncases; i++){
		cin >> n;
		cout << "Case #" << i << ": ";
		countSheep(n);
	}
	return 0;
}
