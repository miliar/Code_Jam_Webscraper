#include <iostream>
#include <algorithm>
#include <vector>
#include <string> 
#include <sstream>

using namespace std;

long long binaryToDigit (long long num) {
	long long ret = 0;
	ostringstream convert;
	convert << num;
	string val = convert.str();
	for(int i = 0; i < val.size(); i++) {
		ret*=2;
		ret+=(long long)(val[i]-'0');
	}

	return ret;

}

long long digitToBinary(long long n) {
	string r;
    while(n!=0) {r=(n%2==0 ?"0":"1")+r; n/=2;}
    return stoll(r);
}

long long convert(int base, long long num) {
	long long ret = 0;
	ostringstream convert;
	convert << num;
	string val = convert.str();
	for(int i = 0; i < val.size(); i++) {
		ret*=base;
		ret+= (long long)(val[i] - '0');

	}
	return ret;
}

bool isPrime(long long num) {
    if (num <= 3) {
        return num > 1;
    } else if (num % 2 == 0 || num % 3 == 0) {
        return false;
    } else {
        for (long long i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

long long divisor(long long num) {
	if (num % 2 == 0) 
    	return 2;
    if (num % 3 == 0) {
        return 3;
    } else {
        for (long long i = 5; i * i <= num; i += 6) {
            if (num % i == 0)
            	return i;
            if (num % (i + 2) == 0) {
                return i+2;
            }
        }
        return -1;
    }
}

int main() {

	int t;
	cin >> t;
	for(int c = t; c<=t; c++) {
		cout << "Case #" << c << ":" << endl;
		int count = 0;
		long long n, j;
		cin >> n >> j;
		long long start = 1;
		for(int i = 1; i < n; i++){
			start*=10;
		}
		long long limit = start*10 + 1;
		start+=1;
		start+=1000000000;
		while(count < j && start < limit) {
			bool prime = false;
			vector<long long> add;
			for(int i = 2; i<=10; i++) {
				long long baseVal;

				baseVal = convert(i,start);
				if(isPrime(baseVal)) {
					prime = true;
					break;
				} else {
					add.push_back(divisor(baseVal));
				}
				if(prime)
					break;
			}
			if(!prime) {
				cout << start;
				for(int j = 0; j < add.size(); j++)
					cout << " " << add[j];
				cout << endl;
				count++;

			}
			long long base2;
			base2 = binaryToDigit(start);
			base2+=2;
			start = digitToBinary(base2);
		}

	}

	return 0;
}
