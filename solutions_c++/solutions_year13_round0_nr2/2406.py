#pragma once

#define _CRT_SECURE_NO_DEPRECATE
#include "targetver.h"

#include <windows.h>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <tchar.h>
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

FILE * in, * out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

int ri() { int a; fscanf(in, "%d", &a ); return a; }
double rf() { double a; fscanf(in, "%lf", &a ); return a; }
char sbuf[100005]; 
string rstr() 
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while(c = fgetc(in))
	{
		if(c == '\n' || c == 255) break;
		*b++=c;
	}
	*b = 0;
	return sbuf; 
}
long long rll() { long long a; fscanf(in, "%lld", &a ); return a; }

int getSym()
{
	fi(5)
	{
		char c = fgetc(in);
		if(c == '.') return 0;
		if(c == 'O') return 1;
		if(c == 'X') return 2;
		if(c == 'T') return 3;
	}
	return 0;
}
int pole[10000];

bool canGrow(int s, int n, int m)
{
	fi(n) 
	{
		bool more = false;
		bool exist = false;
		fj(m)
		{
			if(pole[n*j+i] > s) more = true;
			if(pole[n*j+i] == s) exist = true;
		}

		if(!more && exist)
		fj(m)
			pole[n*j+i] = 0;
	}
	
	fj(m)
	{
		bool more = false;
		bool exist = false;
		fi(n) 
		{
			if(pole[n*j+i] > s) more = true;
			if(pole[n*j+i] == s) exist = true;
		}

		if(!more && exist)
		fi(n) 
			pole[n*j+i] = 0;
	}
	fj(m*n) if(pole[j] == s) return false;
	return true;
}

long _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("B-large (1).in","rt");
	out	= fopen("large_out.txt","wt");
	
	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		int M = ri(); 
		int N = ri(); 
		fj(N*M) pole[j] = ri();

		bool valid = true;
		fj(100) if(!canGrow(j+1, N, M)) { valid = false; break; }

		string result = valid?"YES":"NO";

		fprintf(out, "Case #%d: %s\n",i+1, result.c_str());
		printf("Case #%d: %s\n",i+1, result.c_str());
	}

	fclose(in);
	fclose(out);
	return 0;
}

