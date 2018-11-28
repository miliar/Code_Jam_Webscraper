#include <iostream>
using namespace std;

long long checkDigits(long long a){
	long long result = 0;
	while(a){
		result |= (1<<(a%10));
		a /= 10;
	}
	return result;
}

int main(){
	ios_base::sync_with_stdio(0);
	long long result = 0, tmp, counter, maxi = 0;
	long long t;
	cin >> t;
	for(long long i = 0; i < t; i++){
		result = 0;
		cin >> tmp;
		counter = 1;
		while(result != 1023 && counter < 800){
			result |= checkDigits(counter * tmp);
			counter++;
		}
		cout << "Case #" << i+1 << ":"<<" ";
		if(result != 1023){
			cout << "INSOMNIA";
		} else {
			counter--;
			cout << counter * tmp;// << " " << counter;
		}
		cout << endl;
		// maxi = max(maxi, counter);
	}
	// cout << " max :" << maxi << endl;
	return 0;
}