#include <iostream>
#include <set>
using namespace std;

// function to print a set
void print_set(set<int> S) {
	set<int>::iterator iter;
	for(iter = S.begin(); iter != S.end(); iter++)
		cout << *iter << " ";
	cout << endl;
}

// function to check if a number has exactly the same digits as another one
// but with the difference there it has zeros at the end of it (like 9 and 90)
bool same_digits(long long N, set<int> &used) {
	while(N%10 == 0)
		N = N/10;
	if(used.find(N) != used.end())
		return true;
	used.insert(N);
	return false;
}

// function to insert the digits of N in the set digits
void count_digits(long long N, set<int> &digits) {
	while(N != 0) {
		digits.erase(N%10);
		N = N/10;
	}
}

// count numbers N, 2N, 3N, ... until we have seen all diigits
// in case we cant see all digits, returns -1
long long count_numbers(long long N) {
	int i,k;
	long long last;
	// set with the unseen digits
	set<int> digits;
	// set with the already used numbers N
	set<long long> used;
	for(i = 0; i < 10; i++)
		digits.insert(i);
	// 0 case
	if(N == 0)
		return -1;
	k = 1;
	last = N;
	while(true) {
		//print_set(digits);
		count_digits(last,digits);
		if(digits.empty())
			return last;
		/*if(same_digits(last,used))
			return -1;*/
		k++;
		last = k*N;
	}
	return -1;
}


int main() {
	int T,i;
	long long N,last_number;
	cin >> T;
	for(i = 0; i < T; i++) {
		cin >> N;
		last_number = count_numbers(N);
		cout << "Case #" << i+1 << ": ";
		if(count_numbers(N) == -1)
			cout << "INSOMNIA" << endl;
		else
			cout << last_number << endl;
	}
}