//============================================================================
// Name        : gcj-b.cpp
//============================================================================
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

string patron(short a[],short n,short m)
{
	short l,k,p=0;
	bool flagf =true,flagc = true;
	if(n == 1 || m == 1)
	{
		return "YES";
	}

	//si son cuadradas mira diagonal
	for(int i=0;i<n*m;i++)
	{
		l=a[i];
		k=i;

		//columna
		while(k >= m)
		{
			k=k-m;
		}
		for(int j=0;j<m*n;j=j+m)
		{
			if(l<a[k+j])
			{
				flagc=false;
				break;
			}
		}
		//fila
		k=i;
		if(p<m)
			k=k-p;
		for(int j=0;j<m;j++)
		{
			if(l<a[k+j])
			{
				flagf=false;
				break;
			}

		}
		if(!(flagf) && !(flagc))
			return "NO";
		flagc=true;
		flagf=true;

		if(p == m-1)
			p=0;
		else
			p++;

	}
	if(flagf && flagc)
		return "YES";
	else
		return "NO";
}

int main() {
	int X,T;
	short N,M;

    ofstream fout("D:\\eclipse\\gcj-b\\Debug\\B-large.out");
    ifstream fin("D:\\eclipse\\gcj-b\\Debug\\B-large.in");

   	fin>>T;
    for(X=1;X<=T;X++){
		fin>>N;
		fin>>M;
		short a[N*M];
		for(int i=0;i<N*M;i++)
		{
			fin>>a[i];
		}
		fout<<"Case #"<<X<<": "<<patron(a,N,M)<<endl;

	}

    fout.close();
    fin.close();
   	return 0;
}
