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

//string _tostringlower(string s){for(int i = 0; i<s.length(); i++)	{		if( __isascii(s[i])&& isupper(s[i]))			s[i] = char(_tolower(s[i]));	}	return s;}
//string _tostringupper(string s){	for(int i = 0; i<s.length(); i++)	{		if( __isascii(s[i])&& islower(s[i]))			s[i] = char(_toupper(s[i]));	}	return s;}
vector<string> split( const string& s, const string& delim=" ") {    vector<string> res;    string t;    for ( int i = 0 ; i != s.size() ; i++ ) {        if ( delim.find( s[i] ) != string::npos ) {            if ( !t.empty() ) {                res.push_back( t );                t = "";            }        } else {            t += s[i];        }    }    if ( !t.empty() ) {        res.push_back(t);    }    return res;}
vector<string> splitall( const string& s, const string& delim=" ") {    vector<string> res;    string t;    for ( int i = 0 ; i != s.size() ; i++ ) {        if ( delim.find( s[i] ) != string::npos ) {            {                res.push_back( t );                t = "";            }        } else {            t += s[i];        }    }     {        res.push_back(t);    }    return res;}
vector<int> splitInt( const string& s, const string& delim =" " ) {    vector<string> tok = split( s, delim );    vector<int> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atoi( tok[i].c_str() ) );    return res;}
vector<double> splitDouble( const string& s, const string& delim =" " ) {    vector<string> tok = split( s, delim );    vector<double> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atof( tok[i].c_str() ) );    return res;}
vector<int> splitIntall( const string& s, const string& delim =" " ) {    vector<string> tok = splitall( s, delim );    vector<int> res;    for ( int i = 0 ; i != tok.size(); i++ )        res.push_back( atoi( tok[i].c_str() ) );    return res;}
//bool isPrime (int n){   if (n<=1) return false;   if (n==2) return true;   if (n%2==0) return false;   for (int i=3; (i*i)<=n; i+=2)      if (n%i==0)         return false;   return true;}
//vector<bool> sieve(int n){	vector<bool> prime(n+1, true);	prime[0]=false;	prime[1]=false;    for (int i=2; (i*i)<=n; i++)		if (prime[i])			for (int k=i*i; k<=n; k+=i)				prime[k]=false;   return prime;} 
//int GCD(int a, int b){   if (b==0) return a;   return GCD(b,a%b);}
//int LCM(int a, int b){   return b*a/GCD(a,b);}
//bool _endstring(string s, string s2){	if(s2.length()> s.length()) return false;	s = s.substr( s.length()-s2.length());	if(s == s2) return true;	return false;}
//bool _ispalindrome(string s){	int size = s.length();	int size2 = s.length()/2;	for(int i = 0;i<size2; i++){	if(s[i] != s[size-1-i]) return false;	}	return true;	}
//int sdx[] = {-1, 1, 0, 0};
//int sdy[] = { 0, 0,-1, 1};
//int spx[] = { -1, -1, 1, 1};
//int spy[] = { -1, 1, 1, -1};
//int sax[] = {-1, 1, 0, 0, -1, -1, 1, 1};
//int say[] = { 0, 0,-1, 1, -1, 1, 1, -1};[


int _tmain(int argc, _TCHAR* argv[])
{
	FILE * pFile;
	pFile = fopen("B-large.out", "w");
	ifstream in("B-large.in");
	//pFile = fopen("A-large-practice.out", "w");
	//ifstream in("A-large-practice.in");
	//ofstream out("output1.txt");

	string s;
	getline(in,s);
	int n = atoi(s.c_str());
		
	for(int i = 0; i<n; i++)
	{
		fprintf(pFile, "Case #%d: ", i+1);

		vector<double> vd;
		getline(in,s);

		vd = splitDouble(s);
		double C = vd[0];
		double F = vd[1];
		double X = vd[2];
		
		double ans = 0;
		double test = 0;
		double rate = 2.0;
		double time = 0;

		do
		{
			time = X/rate;
			test = C/rate + X/(rate+F);

			if(test < time)
			{
				ans += C/rate;
				rate += F;
			}
			else
			{
				ans += time;
				break;
			}

		} while( time > test);


		fprintf(pFile,"%.7lf", ans);
		
		fprintf(pFile, "\n");
	}

	in.close();

	fclose(pFile);
	return 0;
}
