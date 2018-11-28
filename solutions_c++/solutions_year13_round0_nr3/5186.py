#include <iostream>
#include <cmath>
#include <string>

using namespace std;


bool is_square(int n){
	if (n < 0)	return false;
	int root (round(sqrt(n)));
	return n == root*root;
}

bool is_pali(int n){
	int tmp = n;
	int rem, sum =0;
	while(n != 0){
		rem = n % 10;
		n /= 10;
		sum = sum*10 + rem;
	}
	if (tmp == sum)	return true;
	else return false;
}
bool is_square_of_pali(int n){
	if(is_square (n) == true){
		int root (round(sqrt(n)));
		if(is_pali(root) == true){
			return true;
		}else{
			return false;
		}
	}else{
		return false;
	}
}



int main(){

	unsigned int numCases=0;
	string str;

	int lower, upper, counter = 0 ,result = 0;
	cin >> numCases;
	getline(cin, str); // get rid of the newline char.

	for (int i = 1; i <= numCases; i++){
		//getline(cin, str);
		cin>>lower>>upper;
		result = 0;
		counter = lower;

		while(counter != upper){
			if(is_square_of_pali(counter) == true && is_pali(counter) == true && is_square(counter) == true)	result++;
			counter ++;
		}
		if(is_square_of_pali(counter) == true && is_pali(counter) == true && is_square(counter) == true)	result++;
		
		cout<<"Case #"<<i<<": "<<result<<endl;
	}


	/*
	while(1){
		cin >> numCases;
		if(is_square(numCases) == true){
			cout<<numCases<<"is square"<<endl;
		}else{
			cout<<numCases<<"is NOT square"<<endl;
		}

		if(is_pali(numCases) == true){
			cout<<numCases<<"is pali"<<endl;
		}else{
			cout<<numCases<<"is NOT pali"<<endl;
		}

		if(is_square_of_pali(numCases) == true && is_pali(numCases) == true && is_square(numCases) == true){
			cout<<numCases<<"is ture"<<endl;
		}else{
			cout<<numCases<<"is NOT true"<<endl;
		}
	}
	*/


	return 0;
}