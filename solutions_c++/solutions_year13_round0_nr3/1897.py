//
//  main.cpp
//  FairAndSquare
//
//  Created by dmp on 4/13/13.
//  Copyright (c) 2013 dmp. All rights reserved.
//
#include <stdint.h>
#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

#define Max		101

// Positive integers Number[0] is the lowest digit
typedef unsigned char Number[Max];
int compareNumbers(Number& n1, Number& n2);

void stringToNumber(const string &s, Number& n)
{
	bzero(n, sizeof(n));
	int i;
	for( i =0; i < s.size(); i++)
		n[ s.size() - i - 1] = s[i] - '0';
}

int numberLastDigit(Number& n)
{
	int i = Max - 1;
	while( n[i] == 0) i--;
	
	return i;
}

void numberToString(Number& n, string& s)
{
	s = "";

	int i = numberLastDigit(n);
	char c[2]; c[1] = 0;
	while( i >= 0)
	{
		c[0] =(char)(n[i] + '0');
		s += string(c );
		i--;
	}
}

void readNumber(Number& n) {
	string s;
	cin >> s;

	stringToNumber(s, n);
}

void numberSetZero(Number& n) {
	bzero(&n, sizeof(n));
}

void numberCopy(Number& n, Number& r)
{
	bcopy(&n, &r, sizeof(n));
}

// no check for overflow
void numberInc(Number& n) {
	int i = 0;
	
	while( 1 ) {
		n[i]++;
		if( n[i] > 9)
		{
			n[i] = 0;
			i++;
		}
		else
			break;
	}
}

int64_t numberToInt64(Number&n)
{
	int64_t result = 0;

	int i = Max;
	while( n[i] == 0) i--;
	
	for(int j = i; j >= 0; j--)
	{
		result *= 10;
		result += n[j];
	}
	
	return result;
}

void int64ToNumber(int64_t n, Number& r)
{
	int p = 0;
	numberSetZero(r);
	
	while( n > 0)
	{
		r[p] = n % 10;
		n /= 10;
		p++;
	}
}

bool numberIsPolindrom(Number& n)
{
	int i = numberLastDigit(n);

	int k = 0;
	for(int j = i; j >= i / 2; j--)
	{
		if( n[j] != n[k]) return false;
		k++;
	}
	
	return true;
}

void nextPolindrom(Number& n)
{
	int i = numberLastDigit(n);
	int p = i/2;
	
	for(int j = (i + 1)/2, k = p; j <= i; j++, k--)
	{
		n[j]++;
		n[k] = n[j];
		if(n[j] <= 9) break;

		n[j] = n[k] = 0;
		if(k == 0 )
		{
			numberSetZero(n);
			n[0] = 1;
			n[i + 1] = 1;
			break;
		}
	}
}

void nextPolindromForNumber(Number& n, Number& r)
{
	numberCopy(n, r);
	if(numberIsPolindrom(n)) return;
	
	int i = numberLastDigit(n);
	int p = i/2;
	
	for(int j = (i + 1)/2, k = p; j <= i; j++, k--)
	{
		r[k] = r[j];
	}
	
	int rs = compareNumbers(n, r);
	if( rs ==  -1) return;
	nextPolindrom(r);
}



// 1 if n1 > n2, -1 if n1 < n2, 0 if ==
int compareNumbers(Number& n1, Number& n2)
{
	int i1 = numberLastDigit(n1), i2 = numberLastDigit(n2);
	if( i1 > i2) return 1;
	if( i1 < i2) return -1;
	
	while(i1 >= 0)
	{
		if( n1[i1] > n2[i1]) return 1;
		if( n1[i1] < n2[i1]) return -1;
		i1 --;
	}
	
	return 0;
}

// find approximation for r = sqrt(n), ensure that r^2 <= n
void sqrtApproximationForNumber(Number& n, Number& r)
{
	int k = numberLastDigit(n) + 1; // number of digits
	int v, p;
	numberSetZero(r);
	
	if( (k % 2) == 0)
	{
		v = (k - 2) / 2;
		p = 3;
	}
	else
	{
		v = (k - 1) / 2;
		p = 1;
	}
	
	r[v] = p;
}

void sqrForNumber(Number & n, Number& r)
{
	int64_t t = numberToInt64(n);
	int64ToNumber(t * t, r);
}

void TestPolindrom(Number& n)
{
	string s;
	numberToString(n,s);
	
	cout << "Number: " << s << " is " << (numberIsPolindrom(n)?"polindrom\n":"not polindrom\n");
}

char CharForResult(int result)
{
	switch(result)
	{
		case 1: return '>';
		case -1:return '<';
		case 0: return '=';
	}
	
	return '?';
}

void TestCompare(Number& n1, Number& n2)
{
	int r;
	string s1, s2;
	
	numberToString(n1, s1);
	numberToString(n2, s2);
	
	r = compareNumbers(n1, n2);
	cout << "Compare: " << s1 << CharForResult(r) << s2 << endl;

	r = compareNumbers(n2, n1);
	cout << "Compare: " << s2 << CharForResult(r) << s1 << endl;

	r = compareNumbers(n1, n1);
	cout << "Compare: " << s1 << CharForResult(r) << s1 << endl;
}

void TestSqrt(Number& n)
{
	Number r;
	string s1, s2;
	
	sqrtApproximationForNumber(n, r);

	numberToString(n, s1);
	numberToString(r, s2);

	cout << "sqrt(" << s1 << ") = " << s2 << endl;
}

void TestInt64(int64_t n)
{
	Number r;
	string s;

	int64ToNumber(n, r);
	
	numberToString(r,s);
	cout << "TestInt64: " << n <<  "  -  " << s << endl;
}

void TestSqr(Number& n)
{
	Number r;
	string s1, s2;
	
	sqrForNumber(n, r);
	
	numberToString(n, s1);
	numberToString(r, s2);
	
	cout << "sqr(" << s1 << ") = " << s2 << endl;
}

void TestNextPalindromNum(Number& n)
{
	Number r;
	string s1, s2;
	
	nextPolindromForNumber(n, r);
	
	numberToString(n, s1);
	numberToString(r, s2);
	
	cout << "nextPalNum(" << s1 << ") = " << s2 << endl;
}

void PrintNumber(const char* prefix, Number& n)
{
	string s;
	numberToString(n, s);
	
	cout << prefix << s << endl;
}

int mainTest(int argc, const char * argv[])
{
	Number n;
	string s;
	
	stringToNumber(string("123454321"), n);numberToString(n,s); cout << s << endl;
	TestPolindrom(n);

	stringToNumber(string("12344321"), n);numberToString(n,s); cout << s << endl;
	TestPolindrom(n);

	stringToNumber(string("12349"), n);	numberInc(n);numberToString(n,s); cout << s << endl;
	int64_t i = numberToInt64(n);cout << i << endl;

	stringToNumber(string("99999"), n);	numberInc(n);numberToString(n,s); cout << s << endl;
	i = numberToInt64(n);cout << i << endl;
	
	TestPolindrom(n);
	
	cout << "\nPolindroms\n";
	
	stringToNumber(string("1"), n);
	for(int i = 0; i < 10; i++ )
	{
		nextPolindrom(n);
		TestPolindrom(n);
	}

	stringToNumber(string("11"), n);
	for(int i = 0; i < 10; i++ )
	{
		nextPolindrom(n);
		TestPolindrom(n);
	}
	
	Number n2;
	stringToNumber(string("12345"), n);
	stringToNumber(string("1234543"), n2);
	
	TestCompare(n, n2);

	stringToNumber(string("12346"), n2);
	TestCompare(n, n2);

	stringToNumber(string("1000"), n2);
	TestCompare(n, n2);

	stringToNumber(string("10"), n);
	TestSqrt(n);
	
	stringToNumber(string("100"), n);
	TestSqrt(n);
	
	stringToNumber(string("1000"), n);
	TestSqrt(n);

	stringToNumber(string("10000"), n);
	TestSqrt(n);

	
	TestInt64(1);
	TestInt64(10);
	TestInt64(99);
	
	stringToNumber(string("1"), n);
	TestSqr(n);
	
	stringToNumber(string("10"), n);
	TestSqr(n);

	stringToNumber(string("100"), n);
	TestSqr(n);
	
	stringToNumber(string("1"), n);
	TestNextPalindromNum(n);

	stringToNumber(string("120"), n);
	TestNextPalindromNum(n);

	stringToNumber(string("1200"), n);
	TestNextPalindromNum(n);

	stringToNumber(string("122"), n);
	TestNextPalindromNum(n);

	stringToNumber(string("1999"), n);
	TestNextPalindromNum(n);
	
	return 0;
}

void processCase()
{
	int64_t count = 0;
	
	string sA, sB;
	Number A, B;
	
	cin >> sA;
	cin >> sB;
	
	// sA = "10";
	// sB = "100000000000000";
	
	stringToNumber(sA, A);
	stringToNumber(sB, B);

	
	Number n, r, rs;
	sqrtApproximationForNumber(A, n); // initial approximation
	nextPolindromForNumber(n, r);
	int rx;

	do {
		sqrForNumber(r, rs);
		rx = compareNumbers(rs, A);	// rs > A = 1
		if( rx != -1) break;
		nextPolindrom(r);
	} while ( 1 );
	
	// PrintNumber("I1: ", r);
	
	do {
		rx = compareNumbers(rs, B);	// rs > A = 1
		if (rx == 1)  break;

		if(numberIsPolindrom(rs))
		{
			//		PrintNumber("PL: ", rs);
			count++;
		}
		
		nextPolindrom(r);
		sqrForNumber(r, rs);

	} while ( 1 );
	
	cout << count;
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		processCase();
		printf("\n");
	}
	
    return 0;
}

int mainT(int argc, const char * argv[])
{
	processCase();
	return 0;
}

