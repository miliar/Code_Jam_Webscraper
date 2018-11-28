#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

vector<long> prime;

bool isPrime(long N, long &divisor);
long findNextPrime(long num);
void fillPrime(long N);
int checkStr(string);

int main() {
	prime.push_back(2);
	prime.push_back(3);

	fstream fin;
	fin.open("input.txt", ios::in | ios::out);

	int t;
	fin >> t;

	int n, j, num_of_zeroes, num_of_ones_minus_two, found;
	string str;
	for (int i = 0; i < t; i++) {
		fin >> n >> j;

		cout << "Case #" << (i+1) << ": " << endl;

		found = 0;
		for (num_of_zeroes = (n-2); num_of_zeroes >= 0 && found < j; num_of_zeroes--) {
			num_of_ones_minus_two = n - num_of_zeroes - 2;
			str = (num_of_zeroes ? string(num_of_zeroes, '0') : "") +
                              (num_of_ones_minus_two ? string(num_of_ones_minus_two, '1') : "");
			found += checkStr(str);
		}
	}

	fin.close();

	return 0;
}

void fillPrime(long N) {
    long num, temp;
    if (prime.back() > N) {
        return;
    }
    
    do {
        temp = prime.back();
        num = findNextPrime(temp);
        if (num <= N) {
            prime.push_back(num);
        }
    } while (num < N);
}

bool isPrime(long N, long &divisor) {
    if (N == 2 || N == 3) {
        return true;
    }
    
    if (N % 2 == 0) {
	divisor = 2;
        return false;
    }
    
    for(long i = 3; i * i <= N; i += 2) {
        if (N % i == 0) {
	    divisor = i;
            return false;
        }
    }
    
    return true;
}

long findNextPrime(long num) {
    num += 2;
    long div;
    while (!isPrime(num, div)) {
        num += 2;
    }
        
    return num;
}

int checkStr(string str) {
	int found = 0, size = str.size();
	string number_str, next_perm = str;
	long num, divisor;
	vector<long> divisors;
	int *num_arr = new int[size];
	bool is_prime = false;
	const char* const_str = str.c_str();

	for (int i = 0; i < size; i++)	{
		num_arr[i] = const_str[i] - '0';
	}

	do {
		number_str = "1" + next_perm + "1";
		divisors.clear();

		for (int base = 2; base <= 10; base++) {
			num = strtol(number_str.c_str(), NULL, base);
			if (isPrime(num, divisor)) {
				is_prime = true;
				break;
			}
			divisors.push_back(divisor);
		}

		if (!is_prime) {
			found ++;

			cout << number_str;
			for (int i = 0; i < divisors.size(); i++) {
				cout << " " << divisors[i];
			}
			cout << endl;
		}

		next_permutation(num_arr, num_arr+size);

		stringstream s;
		for (int i = 0; i < size; i++) {
			s << num_arr[i];
		}

		next_perm = s.str();

	} while (next_perm != str);

	delete num_arr;

	return found;
}
