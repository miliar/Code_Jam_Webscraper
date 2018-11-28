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
	pFile = fopen("A-small-practice.out", "w");
	ifstream in("A-small-attempt0.in");
	//pFile = fopen("A-large-practice.out", "w");
	//ifstream in("A-large-practice.in");
	//ofstream out("output1.txt");

	string s;
	getline(in,s);
	int n = atoi(s.c_str());
		
	for(int i = 0; i<n; i++)
	{
		fprintf(pFile, "Case #%d: ", i+1);

		int x,y;
		vector< vector <int> > vii;
		vector< vector <int> > vii2;
		getline(in, s);
		x = atoi(s.c_str());
		vector<int> ans;

		for(int i = 0; i<4; i++)
		{
			getline(in, s);
			vii.push_back( splitInt(s));
		}

		getline(in, s);
		y = atoi(s.c_str());

		for(int i = 0; i<4; i++)
		{
			getline(in, s);
			vii2.push_back( splitInt(s));
		}

		for(int i = 0; i<4; i++)
		{
			for(int j = 0; j<4; j++)
			{
				if(vii[x-1][i] == vii2[y-1][j])
				{
					ans.push_back(vii[x-1][i]);
				}
			}
		}

		//"Bad magician!"
		//
		if(ans.size() == 1)
		{
			fprintf(pFile, "%d", ans[0]);
		}
		else if(ans.size() > 1)
		{
			fprintf(pFile, "Bad magician!");
		}
		else if(ans.size() == 0 )
		{
			fprintf(pFile,"Volunteer cheated!");
		}

		
		fprintf(pFile, "\n");
	}

	in.close();

	fclose(pFile);
	return 0;
}
