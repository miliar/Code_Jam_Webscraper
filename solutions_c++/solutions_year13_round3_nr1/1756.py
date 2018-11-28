#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

bool cons(char c)
{
	if(c!='a' && c!='e' && c!='i' && c!='o' && c!='u')
		return true;
	else
		return false;
}

bool ok(char str[], int size, int n)
{
	int nr = 0, max = -100;
	
	for(int i=0; i<=(size-n); i++)
	{
		bool flag = true;
		for(int j=i; j<=i+(n-1); j++)
			if(!cons(str[j]))
			{
				flag = false;
				break;
			}	
		if(flag)
			return true;
	}	
	
	return false;
}

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	
	int L, T, n, n_value;
	char c[1000];

	
	//Read
	fin>>T;
	

	//Compute
	for(int t=1; t<=T; t++)
	{
		fin>>c>>n;
		L = strlen(c);
		n_value = 0;
		
		for(int i=0; i<=(L-n); i++)
			for(int j=i+(n-1); j<L; j++)
			{
				char aux[1000];
				int s = -1;
				for(int k=i; k<=j; k++)
					aux[++s] = c[k];
				if(ok(aux, s+1, n))
					n_value++;
			}
		
		//Print	
		fout<<"Case #"<<t<<": "<<n_value<<'\n';
	}	
}