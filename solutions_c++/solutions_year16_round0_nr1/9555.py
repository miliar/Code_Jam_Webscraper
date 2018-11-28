// Google Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

#include <cassert>


typedef long long LL;

//string _tostringlower(string s){for(int i = 0; i<s.length(); i++)	{		if( __isascii(s[i])&& isupper(s[i]))			s[i] = char(_tolower(s[i]));	}	return s;}
//string _tostringupper(string s){	for(int i = 0; i<s.length(); i++)	{		if( __isascii(s[i])&& islower(s[i]))			s[i] = char(_toupper(s[i]));	}	return s;}
vector<string> split( const string& s, const string& delim=" ") {    vector<string> res;    string t;    for ( int i = 0 ; i != s.size() ; i++ ) {        if ( delim.find( s[i] ) != string::npos ) {            if ( !t.empty() ) {                res.push_back( t );                t = "";            }        } else {            t += s[i];        }    }    if ( !t.empty() ) {        res.push_back(t);    }    return res;}
vector<string> splitall( const string& s, const string& delim=" ") {    vector<string> res;    string t;    for ( int i = 0 ; i != s.size() ; i++ ) {        if ( delim.find( s[i] ) != string::npos ) {            {                res.push_back( t );                t = "";            }        } else {            t += s[i];        }    }     {        res.push_back(t);    }    return res;}
vector<int> splitInt( const string& s, const string& delim =" " ) {    vector<string> tok = split( s, delim );    vector<int> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atoi( tok[i].c_str() ) );    return res;}
vector<double> splitDouble( const string& s, const string& delim =" " ) {    vector<string> tok = split( s, delim );    vector<double> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atof( tok[i].c_str() ) );    return res;}
vector<int> splitIntall( const string& s, const string& delim =" " ) {    vector<string> tok = splitall( s, delim );    vector<int> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atoi( tok[i].c_str() ) );    return res;}
//vector<long long> splitLongall( const string& s, const string& delim =" " ) {    vector<string> tok = splitall( s, delim );    vector<long> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atol( tok[i].c_str() ) );    return res;}
//bool isPrime (int n){   if (n<=1) return false;   if (n==2) return true;   if (n%2==0) return false;   for (int i=3; (i*i)<=n; i+=2)      if (n%i==0)         return false;   return true;}
//vector<bool> sieve(int n){	vector<bool> prime(n+1, true);	prime[0]=false;	prime[1]=false;    for (int i=2; (i*i)<=n; i++)		if (prime[i])			for (int k=i*i; k<=n; k+=i)				prime[k]=false;   return prime;} 
int GCD(int a, int b){   if (b==0) return a;   return GCD(b,a%b);}
long long GCD2(long long a, long long b){   if (b==0) return a;   return GCD2(b,a%b);}
//int LCM(int a, int b){   return b*a/GCD(a,b);}
//bool _endstring(string s, string s2){	if(s2.length()> s.length()) return false;	s = s.substr( s.length()-s2.length());	if(s == s2) return true;	return false;}
//bool _ispalindrome(string s){	int size = s.length();	int size2 = s.length()/2;	for(int i = 0;i<size2; i++){	if(s[i] != s[size-1-i]) return false;	}	return true;	}
//int sdx[] = {-1, 1, 0, 0};
//int sdy[] = { 0, 0,-1, 1};
//int spx[] = { -1, -1, 1, 1};
//int spy[] = { -1, 1, 1, -1};
//int sax[] = {-1, 1, 0, 0, -1, -1, 1, 1};
//int say[] = { 0, 0,-1, 1, -1, 1, 1, -1};

int check[10];
int foo()
{
	int res = 0;

	for (int i = 0; i < 10; i++)
	{
		if (check[i] == 0)
		{
			return 0;
		}
	}
	return 1;
}



int _tmain(int argc, _TCHAR* argv[])
{
	string file = "A-large";
	string infile = file + ".in";
	string outfile = file + ".out";
	FILE * pFile;
//	pFile = fopen("out.txt", "w");
//	ifstream in("in.txt");

	
	//pFile = fopen("A-small-attempt0.out", "w");
	//ifstream in("A-small-attempt0.in");
	pFile = fopen(outfile.c_str(), "w");
	ifstream in(infile.c_str());

	/* Start of standard */
	string s;
	getline(in,s);
	int cases = atoi(s.c_str());
	/* End of standard */

	
			
	for(int i_line = 0; i_line<cases; i_line++)
	{
		/* Start of standard */
		fprintf(pFile, "Case #%d: ", i_line+1);
		printf("Case #%d: ", i_line+1);
		/* End of standard */

		for (int x = 0; x < 10; x++)
		{
			check[x] = 0;
		}

		getline(in, s);
		LL N;
		N = atoi(s.c_str());

		LL res = 0;
		LL i = 1;

		res = 0;
		i = 1;
		for (; i < 100000; i++)
		{
			LL x = i*N;

			string test = to_string(x);

			for (LL j = 0; j < test.length(); j++)
			{
				LL y = test[j] - '0';
				check[y] = 1;
			}

			if (i == 89)
			{
				foo();
			}
			if (foo() == 1)
			{
				res = x;
				break;
			}


		}

		if (foo())
		{
			fprintf(pFile, "%d", res);
			printf("%d", res);
	
		}
		else
		{
			fprintf(pFile, "INSOMNIA", res);
			printf("INSOMNIA", res);
		}

		printf("\n");
		fprintf(pFile, "\n");

		/*
		vector<int> vi;
		getline(in,s);
		vi = splitInt(s);

		int R, C, W;
		R = vi[0];
		C = vi[1];
		W = vi[2];
		int res = (R-1)*C + dp[W][C];


		
		*/
	//	fprintf(pFile, "%s", s.c_str());
	//	printf("%s", s.c_str());		 

	//	printf("\n");
	//	fprintf(pFile, "\n");


	}

	in.close();
	fclose(pFile);

	return 0;
}
