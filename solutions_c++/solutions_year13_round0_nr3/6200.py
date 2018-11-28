
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

double _square(unsigned long long val, double tmp) {
	return ( (tmp+(val/tmp))/2);
}

double square(int val) {

	double res = _square(val,1);
	double exres = res*2+1;
	while ( (exres-res) > 0.5) {
		exres = res;
		res = _square(val,res);
	}
	return res;
}

bool isSquare(unsigned long long val) {
	unsigned long long valueInt = (double) square(val);
	return ( (valueInt*valueInt - val) == 0);
}

bool isPalindrome(unsigned long long val) {
	ostringstream oss;
	oss << val;
	string value = oss.str();
	string reverse = value;
	std::reverse(value.begin(), value.end());
	return (value.compare(reverse) == 0);
}


int main() {
	unsigned long long nbTest;
	unsigned long long range_begin, range_end;
	unsigned long long sq_range_begin, sq_range_end;
	unsigned long long cpt;
	unsigned long long beg,end;

	scanf("%d\n",&nbTest);

	for (unsigned long long i=0; i<nbTest; i++) {
		cpt = 0;
		scanf("%d %d",&range_begin, &range_end);

		sq_range_begin = square(range_begin);
		beg = sq_range_begin+1;
		if (isSquare(range_begin) && isPalindrome(sq_range_begin) && isPalindrome(range_begin) ){
			//cout << sq_range_begin*sq_range_begin << " - " << sq_range_begin << " - ";
			//cout << isPalindrome(sq_range_begin) << " - " << isPalindrome(sq_range_begin*sq_range_begin) << endl;
			cpt++;

		}
		sq_range_end = square(range_end);
		end = sq_range_end;
		if (isSquare(range_end) && isPalindrome(sq_range_end) && isPalindrome(range_end)){
			//cout << sq_range_end*sq_range_end << " - " << sq_range_end << " - ";
			//cout << isPalindrome(sq_range_end)  << " - " << isPalindrome(sq_range_end*sq_range_end) << endl;
			cpt++;
			end = sq_range_end-1;
		}
		//cout << "end" << end << endl;
		if ((sq_range_end == sq_range_begin) && isSquare(range_end)) {
			cpt = 1;
		}


		for (unsigned long long j= beg; j<= end; j++) {
			//cout << "test " << j*j  <<" " << j<<endl;
			if (isPalindrome(j)) {
				if (isPalindrome(j*j)) {
					//cout << j*j << " - " << j << " - ";
					//cout << isPalindrome(j) << " - " << isPalindrome(j*j) << endl;
					cpt++;
				}
			}
		}

		cout << "Case #" << (i+1) << ": " << cpt << endl;
	}
}
