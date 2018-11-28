#include <iostream>
#include <math.h>

using namespace std;

long long NUM = 1000000000000001;

void Update_Number()
{
	int mod;
	for(int i = 2; i < 16; ++i) {
		mod = (int)(NUM % (long long)pow(10,i)) / pow(10,i-1);
			if(mod) {
				NUM = NUM - (long long)pow(10,i-1);
			}
			else {
				NUM += (long long)pow(10,i-1);
				return;
			}
	
	}

}


long long check_prime(long long n) 
{
	if(n % 2 == 0)
		return 2;
	for(long long i = 3; i <= sqrt(n); i += 2) {
		if(n % i == 0)
			return i;
	}
	return -1;
}


int main()
{
	int t; cin >> t;
	int digits, number;
	cin >> digits >> number;

	while(t) {

		cout << "Case #1:"<< endl;

	for(int q = 0; q < number;) {


		Update_Number();
		long long allnums[9] = {0,0,0,0,0,0,0,0,0};
		long long tempnum;
		for(int j = 2; j <= 10; ++j) {
			tempnum = NUM;
			for(int i = 0; i < digits; i++) {
				if(tempnum % 10)
					allnums[j-2] += pow(j,i);
				tempnum /= 10;
			}
		}

		bool notproper = false;
		long long factors[9] = {0,0,0,0,0,0,0,0,0};
		long long temp;
		for(int i = 0; i < 9; ++i) {
			temp = check_prime(allnums[i]);
			if(temp != -1) {
				factors[i] = temp;
			} else {
				break;
				notproper = true;
			}
			
			if(!notproper and i == 8) {
				cout << NUM << " ";
				for(int i = 0; i < 9; ++i) {cout << factors[i] << " ";}
				cout << endl;
				++q;
			}

		}

	}

	t--;}
	

	return 0;
}