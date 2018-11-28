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


struct Variant
{
	int numb[10];
	double prob;
};

__int64 fac(int i)
{
	if(i <= 1) return 1;
	return fac(i-1)*i;
}

void generateVariants(Variant & cur, int pos, int sum, double prob, int N, int M, vector<Variant> & out)
{
	if(pos == M)
	{
		cur.numb[pos] = sum;
		cur.prob = prob*fac(sum);
		out.push_back(cur);
		return;
	}

	fi(sum+1)
	{
		cur.numb[pos] = i;
		generateVariants(cur,pos+1,sum-i,prob*fac(i),N,M,out);
	}
}

void generateVariants2(Variant & cur, __int64 umn, int pos, int sum, double prob, int N, int M, vector<Variant> & out)
{
	if(pos == M+1)
	{
		if(umn != 1) return;

		cur.prob = sum;
		out.push_back(cur);
		return;
	}


	fi(sum+1)
	{
		cur.numb[pos] = i;
		generateVariants2(cur,umn,pos+1,sum-i,prob*fac(i),N,M,out);
		if( (umn%pos) != 0 ) return;
		umn /= pos;
	}
}

void adjustProb(vector<Variant> & all, vector<Variant> & cur, vector<double> & pr, int M)
{
	fi(all.size())
	{
		if(pr[i] == 0) continue;
		bool iscorrect = false;
		fj(cur.size())
		{
			bool correct = true;
			for(int k = 2; k<=M; k++)
			{
				correct = correct && (all[i].numb[k] >= cur[j].numb[k]);
			}
			iscorrect = correct;
			if(iscorrect) break;
		}
		if(!iscorrect ) pr[i] = 0;
	}
}

long _tmain(int argc, _TCHAR* argv[])
{
	in	= fopen("C-small-1-attempt0.in","rt");
	out	= fopen("small1_out.txt","wt");

	int T = ri(); 
	for(int i = 0; i<T; i++)
	{
		int R = ri(); 
		int N = ri(); 
		int M = ri(); 
		int K = ri(); 

		vector<Variant> variants;
		Variant cur;
		generateVariants(cur,2,N,1,N,M,variants);


		fprintf(out, "Case #%d:",i+1);
		printf("Case #%d:",i+1);
		printf("\n");
		fprintf(out, "\n");

		fk(R)
		{
			vector<double> pr(variants.size());
			fj(variants.size()) pr[j] = 1;

			fj(K)
			{
				__int64 lli = rll();
				vector<Variant> variants2;
				generateVariants2(cur,lli,2,N,1,N,M,variants2);
				adjustProb(variants,variants2, pr, M);
			}
			double maxpr = 0;
			int maxi = 0;

			fj(variants.size())
				if(pr[j]*variants[j].prob > maxpr)
				{
					maxpr = pr[j]*variants[j].prob;
					maxi = j;
				}
			for(int j = 2; j<= M; j++)
			{
				for(int s = 0; s<variants[maxi].numb[j]; s++)
				{
					fprintf(out,"%d",j);
					printf("%d",j);
				}
			}
			printf("\n");
			fprintf(out, "\n");
		}
	
		
	
		fprintf(out, "\n");
		printf("\n");
		
	}

	fclose(in);
	fclose(out);
	return 0;
}

