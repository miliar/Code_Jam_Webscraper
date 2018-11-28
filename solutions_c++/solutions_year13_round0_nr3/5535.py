#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

int t, a, b, n, m, i, j, aux_t = 1, rez; 

bool palindrom(int x)
{
	int v[10], s = 0;
	
	while(x)
	{
		v[++s] = x%10;
		x /= 10;
	}
	for(int i=1; i<=s/2; i++)
		if(v[i] != v[s-i+1])
			return false;
			
	return true;
}

bool fair(int x)
{
	float z = sqrt(x);
	if(z != (int)z)
		return false;
	if(palindrom(z))
		return true;
	else
		return false;
}

int fair_and_square()
{
	int nr = 0;
	
	for(i=a; i<=b; i++)
		if(palindrom(i) && fair(i))
			nr++;
				
	return nr;
}

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	
	//Read
	
	fin>>t;
	
	
	//Compute
	while(aux_t <= t)
	{
		fin>>a>>b;
		fout<<"Case #"<<aux_t<<": "<<fair_and_square()<<"\n";
		aux_t++;
	}
}