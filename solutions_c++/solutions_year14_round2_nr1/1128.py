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
	//pFile = fopen("out.txt", "w");
	//ifstream in("in.txt");
	pFile = fopen("A-large.out", "w");
	ifstream in("A-large.in");


	string s;
	getline(in,s);
	int cases = atoi(s.c_str());
		
	for(int i_line = 0; i_line<cases; i_line++)
	{
		fprintf(pFile, "Case #%d: ", i_line+1);

		getline(in,s);
		int n = atoi(s.c_str());
		int ans = 0;
		vector<string> vs;
		for(int i = 0; i<n; i++)
		{
			getline(in,s);
			vs.push_back(s);
		}
		
		char c = ' ';
		for(int i = 0; i<vs[0].size(); i++)
		{
			if(i == 0 )
			{
				c = vs[0][i];
			}


		}

		do
		{
			c = vs[0][0];
			vector<int> vi;
			int count = 0;
			for(int i = 0; i<vs.size();i++)
			{
				count = 0;

				for(int j = 0; j<vs[i].size();)
				{
					if(c == vs[i][j])
					{
						count ++;
						vs[i].erase(vs[i].begin());
					}
					else
					{
						break;
					}
				}

				if(count == 0)
				{
					ans = -1;
					break;
				}
				else
				{
					vi.push_back(count);
				}
			}

			sort(vi.rbegin(), vi.rend());
				
			int minx = 100000;
			int temp = 0;
			for(int i = 0; i<=vi[0]; i++)
			{
				temp = 0;
				for(int j = 0; j<vi.size(); j++)
				{
					temp += abs(i - vi[j]);
				}
				minx = min(minx, temp);
				
			}
			ans += minx;

			vi.clear();

		} while (vs[0].size()>0);
		
		for(int i = 0; i<vs.size(); i++)
		{
			if(vs[i].size() > 0)
			{
				ans = -1;
				break;
			}
		}
		
		if(ans == -1)
		{
			fprintf(pFile, "Fegla Won");
		}
		else
		{
			fprintf(pFile, "%d", ans);
		}

		fprintf(pFile, "\n");

		//
	}

	in.close();

	fclose(pFile);
	return 0;
}
