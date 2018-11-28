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


unsigned __int64 invert(unsigned __int64 i, unsigned __int64 & mn)
{
	unsigned __int64 res = 0;
	mn = 1;
	while(i)
	{
		mn  *= 10;
		res *= 10;
		res += (i%10);
		i /= 10;
	}
	return res;
}

vector<unsigned __int64> numbers;

void fillallsquares()
{
	int count = 0;
	for(unsigned __int64 i = 0; i<100000; i++)
	{
		if( (i%100000) == 0) printf("%d\n",i*100/10000000);
		unsigned __int64 mn, d;
		unsigned __int64 k = invert(i, mn);
		if(i != invert(k, mn)) continue;
		unsigned __int64 kv = (i+k*mn)*(i+k*mn);
		if(kv == invert(kv, d) && kv)
		{
			count ++;
			printf("%lld %lld\n",i+k*mn, kv);
			numbers.push_back(kv);
		}
		fj(10)
		{
			kv = (i+k*10*mn+j*mn)*(i+k*10*mn+j*mn);
			if(kv == invert(kv, d) && kv)
			{
				count ++;
				printf("%lld %lld\n",i+k*10*mn+j*mn, kv);
				numbers.push_back(kv);
			}
		}
	}
	printf("%d\n",count);
}

unsigned __int64 readNotSoLongInt()
{
	int numDigits = 0;
	int c;
	__int64 res = 0;
	while( (c = fgetc(in)) != 0 && !isalnum(c));

	do
	{
		res *= 10;
		res += c-'0';
		numDigits ++;
	}
	while( (c = fgetc(in)) != 0 && isalnum(c));
	
	if(numDigits > 15) // uper bound is not important
		return 100000000000000000ULL;
	return res;
}

long _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("C-small-attempt0 (1).in","rt");
	out	= fopen("small_out.txt","wt");
	fillallsquares();

	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		int sum = 0;
		__int64 f = readNotSoLongInt();
		__int64 l = readNotSoLongInt();

		fj( (numbers.size()) ) if(numbers[j] >= f && numbers[j] <= l) sum ++;
		fprintf(out, "Case #%d: %d\n",i+1, sum);
		printf("Case #%d: %d\n",i+1, sum);
	}

	fclose(in);
	fclose(out);
	return 0;
}

