#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>
using namespace std;


int main()
{
	FILE* fin =fopen( "input.in" , "r");
	FILE* fout =fopen( "output.out" , "w");
	int t , tt=0;


	fscanf(fin , "%d", &t);
	while(tt++<t)
	{
		long long r,lit , p=0 , rr , painted=0;
		fscanf(fin , "%lld %lld", &r , &lit);
		rr = r+1;

		do
		{
			p += (rr*rr - r*r);
			rr+=2;
			r+=2;
			if(p<= lit)
				painted++;
		}while(p <= lit);

		fprintf(fout , "Case #%d: %lld\n" , tt , painted);


	}
	return 0;
}