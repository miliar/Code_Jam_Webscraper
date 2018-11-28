/*
 * fair-sqare.cpp
 *
 *  Created on: Apr 14, 2013
 *      Author: saha
 */



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <queue>

using namespace std;
typedef long long mylong;

bool is_palindrome(mylong n)
{
	ostringstream st; st<<n;
	string s = st.str();

	bool pal = true;
	for(int i = 0, j = s.length()-1; i<j ; i++, j--) {
		if(s[i] != s[j]) {
			pal = false;
			break;
		}
	}
//	if(pal)
//		cout << "One palindrome detected is : " << n << endl;
	return pal;
}

int main()
{
	int T;
	mylong A, B;
	mylong a,b;

	long double sa, sb;

	scanf("%d", &T);
	scanf("\n");
	for(int t=1; t<=T ; t++, scanf("\n")) {
		scanf("%lld %lld",&A,&B);
		scanf("\n");

		sa = sqrtl(A);
		sb = sqrtl(B);

		a = sa;
		b = sb;

		if(a*a < A)
			a++;

		mylong count = 0;
		for (mylong i=a; i<=b ; i++) {
			if(!is_palindrome(i))
				continue;
			mylong n = i*i;
			if(is_palindrome(n))
				count++;
		}

		printf("Case #%d: %lld\n", t, count);
	}
}



