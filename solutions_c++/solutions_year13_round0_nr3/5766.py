#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int M,N ,k,h;
int arr[101][101];
bool c=true;

int isp(char s[222]) {
	int i = -1, j = strlen(s);
	while (i < j && s[++i] == s[--j]);
	return i >= j;
}

int main()
{
	ifstream fin ("in.txt");
	ofstream fout("out.txt");
	int n,TT=0,counter=0;

	fin>>n;
	while(TT<n)
	{
		counter = 0;
		fin>>N>>M;
		TT++;
		for (int i = N; i<=M; i++)
			{
				char s1[222] , s2[222];
				sprintf(s1 , "%d" , i);
				int j = sqrt(double(i));
				if(j*j == i)
				{
					sprintf(s2 , "%d" , j);
					if (isp(s1) && isp(s2))
					counter++;
				}
			}
		fout<<"Case #"<<TT<<": "<<counter<<"\n";
	}
	return 0;
}

