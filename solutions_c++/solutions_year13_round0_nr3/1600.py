#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>

using namespace std;
#define MAX_DIGITS 100
int checkPalindrome(int);
int checkPalindromeSquare(int);

int main() {
	int number = 0;
	
	string str = "";
	while (true) {
		getline(cin, str);

		stringstream stream(str);
		if (stream >> number)
			break;
	}
	
	for(int k = 0; k < number; k++) {
		if(k != 0)
			cout << endl;
		getline(cin, str);
		string buf;

		istringstream ss(str);
		vector<double> tokens;
		copy(istream_iterator<double>(ss), istream_iterator<double>(), back_inserter<vector<double>>(tokens));
		double min = tokens[0];
		double max = tokens[1];

		int minSqrt = ceil(sqrt(double(min)));
		int maxSqrt = floor(sqrt(double(max)));
		int total = 0;

		for(int j = minSqrt; j <= maxSqrt; j++) {
			if(checkPalindrome(j) == 1) {
				total += checkPalindromeSquare(j);
				if(j >= 10 && j <= 99) {
					if(j > 90)
						j += 1;
					else
						j += 10;
				} else if(j >= 100 && j <= 999) {
					if(j % 1000 >= 990)
						j += 1;
					else
						j += 9;
				} else if(j >= 1000 && j <= 9999) {
					if(j % 10000 >= 9990)
						j += 1;
					else if(j % 100 >= 90)
						j += 10;
					else
						j += 109;
				} else if(j >= 10000 && j <= 99999) {
					if(j % 100000 >= 99990)
						j += 1;
					else if(j % 10000 >= 9990)
						j += 10;
					else
						j += 99;
				} else if(j >= 100000 && j <= 999999) {
					if(j % 1000000 >= 999990)
						j += 1;
					else if(j % 100000 >= 99990)
						j += 10;
					else if(j % 10000 >= 9900)
						j += 109;
					else
						j += 1099;
				} else if(j >= 1000000 && j <= 9999999) {
					if(j % 1000000 >= 999990)
						j += 10;
					else if(j % 100000 >= 99900)
						j += 109;
					else if(j % 10000 >= 9000)
						j += 1099;
					else
						j += 999;
				}
			}
		}
		cout << "Case #" << k + 1 << ": " << total;
	}
	return 0;
}

int checkPalindrome(int number) {
	int n1, rev = 0, rem;
	n1 = number;
	while (n1 > 0){
		rem = n1 % 10;
		rev = rev * 10 + rem;
		n1 = n1 / 10;
	}
	if (number == rev){
		return 1;
	}
	return 0;
}

int checkPalindromeSquare(int number) {	
	int             a[MAX_DIGITS];
	int             b[MAX_DIGITS];
	int             r[6 * MAX_DIGITS];
	int             d_a;
	int             d_b;
	int             d;

	int             i;

	int n2 = number;
	d_a = 0;
	i = 0;
	while(n2 > 0) {
		a[d_a] = n2 % 10;
		b[d_a] = n2 % 10;
		++(d_a);
		n2 /= 10;
	}

	for(d = 1; d < d_a; d *= 2);
	for(i = d_a; i < d; i++) a[i] = 0;

	d_b = d_a;
	for(i = d_b; i < d; i++) b[i] = 0;

	void gradeSchool(int *a, int *b, int *ret, int d);
	void doCarry(int *a, int d);
	gradeSchool(a, b, r, d); 
    doCarry(r, 2 * d);
	/*void printNum(int *, int);
	printNum(r, 2 * d);
	*/
	bool checkPalindromeBool(int *, int);
	if(checkPalindromeBool(r, 2 * d)) {
		return 1;
	}
	return 0;
}

bool checkPalindromeBool(int *r, int d) {
	int i;
    for(i = d - 1; i > 0; i--) if(r[i] != 0) break;
	d = 0;
	for(; i >= d; i--, d++) {
		if(r[i] != r[d])
			break;
	}
	if(i >= d)
		return false;
	return true;
}
/*
void printNum(int *a, int d) {
    int i;
    for(i = d - 1; i > 0; i--) if(a[i] != 0) break;
    for(; i >= 0; i--) printf("%d", a[i]);
}
*/
void gradeSchool(int *a, int *b, int *ret, int d) {
    int             i, j;

    for(i = 0; i < 2 * d; i++) ret[i] = 0;
    for(i = 0; i < d; i++) {
        for(j = 0; j < d; j++) ret[i + j] += a[i] * b[j];
    }
}

void doCarry(int *a, int d) {
    int             c;
    int             i;

    c = 0;
    for(i = 0; i < d; i++) {
        a[i] += c;
        if(a[i] < 0) {
            c = -(-(a[i] + 1) / 10 + 1);
        } else {
            c = a[i] / 10;
        }
        a[i] -= c * 10;
    }
}