#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>

extern "C" {
#include <stdint.h>
}

using namespace std;

int64_t val(const string &M)
{
	char *endptr;
	return strtoll(M.c_str(), &endptr, 10);
}

string add(const string &M, const int64_t N)
{
	stringstream ss;
	ss << (val(M) + N);
	return ss.str();
}

string tostr(const int64_t A)
{
	stringstream ss;
	ss << A;
	return ss.str();
}

void split(const string &X, string &l, string &c, string &r)
{
	int n = X.length();
	c = "";
	l = X.substr(0,n/2);
	if ( n%2 == 1) c = X[n/2];
	if ( n%2 == 1)
		r = X.substr(n/2+1,n/2);	
	else 
		r = X.substr(n/2,n/2);	
}

string rev(const string &S)
{
	string R = S;
	reverse(R.begin(), R.end());
	return R;
}

bool ispalin(const string &S)
{
	string l = "", c = "", r = "";
	split(S,l,c,r);
	return l == rev(r);
}

string zero_ext(const string &S, const int L)
{
	string X = "";
	for (int i = 0; i < L; i++) X += '0';
	int n = S.length();
	for (int i = 0; i < n; i++) X[L-1-i] = S[n-1-i];
	return X;
}

string next_palin(const string &N)
{
	string P = "";
	int L = N.length();
	string l = "", c = "", r = "";
	string n_l = "", n_c = "", n_r = "";
	string n_r2 = "";
	split(N,l,c,r);
	n_l = l;
	n_c = c;
	n_r = rev(l);
	
	n_r2 = n_c + n_r;
	string t = add(n_r2,1);
	if (t.length() > n_r2.length()) {  // All '9' case
		string one = zero_ext("1",(L+1)/2);
		if (L % 2 == 1) {
			P = rev(one) + one ;
		} else {
			P = rev(one) + "0" + one; 
		}	
	} else {
		if ( val(r) < val(n_r) ) {
			P = n_l + n_c + n_r;
		} else{
			// increment left parts;
			if (L % 2 == 1) {
				int ncl = n_c.length();
				n_c = add(n_c,1);
				if (int(n_c.length()) > ncl) {
					n_l = add(n_l,1);
					n_c = "0";
					n_r = rev(n_l);
				}
			} else {
				n_l = add(n_l,1);
				n_r = rev(n_l);
			}
			P = n_l + n_c + n_r;
		}

	}

	return P;
}

#if 0
int test(int argc, char *argv[])
{
	string N = "1245";
	string l = "", c = "", r = "";
	cout << add("1234", 13) << endl;
	split(N,l,c,r);
	cout << l << " " << c << " " << r << endl;
	cout << ispalin("1234") << endl;
	cout << ispalin("1221") << endl;
	cout << ispalin("12534") << endl;
	cout << ispalin("12521") << endl;
	cout << zero_ext("13", 1) << endl;
	cout << next_palin("999") << endl;
	cout << next_palin("9999") << endl;
	cout << next_palin("8112") << endl;
	cout << next_palin("81390") << endl;
	cout << next_palin("81990") << endl;
	cout << next_palin("8190") << endl;
	cout << next_palin("2994") << endl;

	string num = "1";
	for (int i = 0; i < 125; i++, num =next_palin(num)) cout << num << endl;

	return 0;
}

#endif


int main(int argc, char *argv[])
{
	int T; cin >> T;
	int64_t A, B;
	int64_t sq_A, sq_B;
	string lb = "", ub ="", s ="";
	int64_t nb = 0;
	int64_t count = 0;
	for (int t = 0; t < T; t++) {
		cin >> A >> B;
		//cout << A << " " << B << endl;
		sq_A = (int64_t) floor(sqrt(A));
		sq_B = (int64_t) ceil(sqrt(B));
		//cout << sq_A << " " << sq_B << endl;
		count = 0;
		for (s = tostr(sq_A); val(s) <= sq_B ; s = next_palin(s) ) {
			nb = val(s);
			if (ispalin(tostr(nb*nb)))  {
				if ((nb * nb >= A) && (nb * nb <= B)) {
					count++;
					//cout << nb << endl;
				}
			}
		}	
		cout << "Case #" << t+1 << ": " << count << endl;
	}



}
