//============================================================================
// Name        : gcj-c.cpp
// Author      : 
//============================================================================
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

bool pali(string n, string r)
{
	int tn,tr;
	tn=(int)n.length();
	tr=(int)r.length();
	if(tn==1)
	{
		if(tr==1)
			return true;
	}
	else
	{
		for(int i=1;i<=tn/2;i++)
		{
			if(n[i-1]!=n[tn-i])
				return false;
		}

		if(tr==1)
			return true;
		else
		{
			for(int j=1;j<=tr/2;j++)
			{
				if(r[j-1]!=r[tr-j])
					return false;
			}
			return true;
		}
	}
	return false;
}

int main() {
	double X,T,A,B;
	int cont=0;
	float r;
	string num,raiz;

    ofstream fout("D:\\eclipse\\gcj-c\\Debug\\C-small-attempt0.out");
    ifstream fin("D:\\eclipse\\gcj-c\\Debug\\C-small-attempt0.in");

    fin>>T;
    for(X=1;X<=T;X++){
		fin>>A;
		fin>>B;
		for(A;A<=B;A++)
		{
			r=sqrt(A);
			stringstream num1,num2;
			num1<< A;
			num=num1.str();
			num2<< r;
			raiz = num2.str();
			if(pali(num,raiz))
				cont++;
		}
		fout<<"Case #"<<X<<": "<<cont<<endl;
		cont=0;
	}

    fout.close();
    fin.close();
   	return 0;
}
