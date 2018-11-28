#include <iostream>
#include <vector>
#include <map>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <math.h>
#include <algorithm>

using namespace std;

int is_not_prime(long number){
	long end = (long)(sqrt(number) + 1);
	for(int i = 2; i <= end; i++){
		if(number % i == 0)
			return i;
	}
	return 0;
}

bool check_for_each_base(char * number, int X){
	//check for base 2
	long base2 = strtol(number, NULL, 2);
	cerr << "Base 2: " << base2 <<endl;

	if((base2 = is_not_prime(base2)) == 0)
		return false;

	long base3 = strtol(number, NULL, 3);
    cerr << "Base 3: " << base3 <<endl;

    if((base3 = is_not_prime(base3)) == 0)
		return false;

	long base4 = strtol(number, NULL, 4);
    cerr << "Base 4: " << base4 <<endl;

    if((base4 = is_not_prime(base4)) == 0)
		return false;

	long base5 = strtol(number, NULL, 5);
    cerr << "Base 5: " << base5 <<endl;

    if((base5 = is_not_prime(base5)) == 0)
		return false;

	long base6 = strtol(number, NULL, 6);
    cerr << "Base 6: " << base6 <<endl;

    if((base6 = is_not_prime(base6)) == 0)
		return false;

	long base7 = strtol(number, NULL, 7);
    cerr << "Base 7: " << base7 <<endl;

    if((base7 = is_not_prime(base7)) == 0)
		return false;

	long base8 = strtol(number, NULL, 8);
    cerr << "Base 8: " << base8 <<endl;

    if((base8 = is_not_prime(base8)) == 0)
		return false;

	long base9 = strtol(number, NULL, 9);
    cerr << "Base 9: " << base9 <<endl;

    if((base9 = is_not_prime(base9)) == 0)
		return false;

	long base10 = strtol(number, NULL, 10);
    cerr << "Base 10: " << base10 <<endl;

    if((base10 = is_not_prime(base10)) == 0)
		return false;

	//Number is not prime in all bases

	cerr << "Factors:" << endl;
	cerr<<"Base2="<<base2<<", Base3="<<base3<<", Base4="<<base4<<", Base5="<<base5<<", Base6="<<base6<<", Base7="<<base7<<", Base8="<<base8<<", Base9="<<base9<<", Base10="<<base10<<endl;

	cout <<number<<" "<<base2<<" "<<base3<<" "<<base4<<" "<<base5<<" "<<base6<<" "<<base7<<" "<<base8<<" "<<base9<<" "<<base10<<endl;

	return true;
}

void decimal_to_binary(unsigned long long number, char* no){
	//char no[256];
	int base = 2;
	stack<int> remainders;
	do{
		remainders.push(number % base);
		number = number / base;
	}while(number != 1);
	remainders.push(number);
	
	int size = remainders.size();
	int i;
	for (i = 0; i < size; i++){
		no[i] = remainders.top() + 48 ;
		remainders.pop();
	}
	no[i] = '\0';

	//return no;
}

int main(){
	int T, N, J, found;
	cin >> T;
	char number[256];
	cerr << "T: " << T << endl;
	for(int X = 1; X <= T; X++){
		cin >> N >> J;
		cerr << "Values: N=" << N << ", J=" << J << endl;
		found = 0;

		//Initialize the string
		for(int i = 0; i < N; i++){
			if(i== 0 || i == N-1){
				number[i] = '1';
			}else{
				number[i] = '0';
			}
		}
		number[N] = '\n';
		cerr << "Initial number: " << number << endl;
		cout <<"Case #" << X << ": " << endl;
	    for (int i = 0; i<10000; i++){
			if(check_for_each_base(number, X)){
				found++;
				if(found >= J)
					break;

			}
			cerr << "Current number (Char): " << number <<endl;	
			unsigned long long next_no = strtol(number, NULL, 2);
			next_no += 2;
			cerr << "Next number (Decimal): " <<next_no <<endl;
			char new_no[256];
			decimal_to_binary(next_no, new_no);
			strcpy(number, new_no);
			cerr << "Next number (Binary):" << *new_no << endl;
			if(next_no == 2)
				break;
		}	
	}
	return 0;
}
