#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <vector>
#include <math.h>
#include <stdint.h>

using namespace std;

unsigned long long int get_power(int power, int base) {
	unsigned long long int result = 1;
	for(int i = 0; i < power; i++) {
		result *= base;
	}
	return result;
}

vector< vector<int> > init(int len) {
	vector< vector<int> > whole;
	unsigned long long int num = get_power(2,len-2);
	for(int i = 0; i < num; i++) {
		vector<int> myVec;
		myVec.push_back(1);
		int ct = len-3;
		while(ct >= 0) {
			unsigned long long int power = get_power(ct,2);
			myVec.push_back(i/power%2);
			ct--;
		}
		myVec.push_back(1);
		whole.push_back(myVec);
	}
	return whole;
}

int isPrime(unsigned long long int number){
    if(number == 2) return -1;
    if(number % 2 == 0) return 2;
    for(int i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) return i;
    }
    return -1;
}

unsigned long long int get_num_by_base(int base, vector<int> number) {
	unsigned long long int result = 0;
	for(int i = 0; i < number.size(); i++) {
		int power = number.size() - 1 - i;
		unsigned long long int mutiplier = get_power(power,base);
		result += mutiplier * number.at(i);
	}
	return result;
}

void jamcoin(vector< vector<int> > vec, int num) {
	for(int i = 0; i < vec.size(); i++) {
		if(num == 0) {
			return;
		}
		vector<int> test = vec.at(i);
		bool cont_flag = true;
		vector<int> factors;
		for(int j = 2; j <= 10; j++) {
			unsigned long long int final_number = get_num_by_base(j,test);
			int prime_flag = isPrime(final_number);
			if(prime_flag == -1) {
				cont_flag = false; // a prime 
				break;
			} else {
				factors.push_back(prime_flag);
				continue;
			}
		}
		if(cont_flag) {
			num--;
			for(int k = 0; k < test.size(); k++) {
				cout << test.at(k);
			}
			cout << " ";
			for(int h = 0; h < factors.size(); h++) {
				cout << factors.at(h) << " ";
			}
			cout << endl;
		}
	}
}

int main() {
	string line;
	int testNum;
	getline(cin, line);
	stringstream ss(line);
	ss >> testNum;
	int ct = 1;
	while(testNum > 0) {
		int len,num;
		getline(cin, line);
		stringstream ss1(line);
		ss1 >> len >> num;
		vector< vector<int> > all = init(len);
		cout << "Case #" << ct << ": " << endl;
		jamcoin(all,num);
		testNum--;
		ct++;
	}
	return 0;
}