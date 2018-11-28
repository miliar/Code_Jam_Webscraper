#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

const int SIZE = 16;
const long long low = 1;
const long long hi = (1LL << SIZE) - 1;
int needed = 50;

string to_binary(long long x)
{
    string s;
    do
    {
        s.push_back('0' + (x & 1));
    } while (x >>= 1);
    std::reverse(s.begin(), s.end());
    return s;

}

bool isPrime(long long n) {
    if (n <= 1)  return false;
    if (n <= 3)  return true;
    if (n%2 == 0 || n%3 == 0) return false;
    for (long long i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
           return false;
    return true;
}

pair<bool, long long> convert(const string& num, long long base) {
	long long cur_mul = 1;
	long long number = 0;
	for (int i = num.size() - 1; i >=0 ; i--) {
		if (num[i] == '1') {
			//cout << "sum " << cur_mul << endl;
			number+= cur_mul;
		}

		cur_mul*= base;
		//cout << cur_mul << endl;
	}
	//cout << "num " << number << endl;
	for (long long div = 3; div <= sqrt(number)+1; div++ ) {
		if (number % div == 0 && div != number) {
			//cout <<" div " << div << endl;
			return make_pair(true, div);
		}
	}
	return make_pair(false, 0);
}
void Generate() {
	for (long long i = low; i <=hi; i++) {
		if (!needed) {
			break;
		}
		if ( (i & 1) == 0) {
			continue;
		}
		if (isPrime(i)) {
			continue;
		}
		string bn = to_binary(i);
		if(bn.size() < SIZE) {
			continue;
		}
		//cout << bn << endl;
		vector<long long> nums;
		for (int base = 2; base <=10; base ++) {
			pair<bool, long long> res = convert(bn, base);
			if(res.first == false) {
				break;
			}
			nums.push_back(res.second);
		}
		if (nums.size() == 9) {
			cout << bn;
			for (auto x : nums) {
				cout <<" "<<x;
			}
			cout << endl;
			needed--;
		}
	}
}
void PrintAnswer(int n, int j) {

}
int main() {
	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);

	int t, n, j;
	cin >> t >> n >> j;
	cout << "Case #" << 1 <<":\n";
	Generate();
	return 0;
}
