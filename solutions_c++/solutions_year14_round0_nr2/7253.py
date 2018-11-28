#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <map>
#include <stack>
#include <iomanip>
#define s(T) scanf("%d",&T)
#define ls(T) scanf("%ld",&T)
#define us(T) scanf("%u",&T)
#define uls(T) scanf("%lu",&T)
#define SIZE 65535
#define mx 10
using namespace std;
int main()
{
	double c,x,f,s,fi;
	int i,j,T,p,q,k;
	ifstream filei ("B-large.in");
	ofstream fileo ("output.txt");
	filei>>p;
	T=p;
	for(k=1; k<=T; ++k)
    {
        filei>>c>>f>>x;
        fi=2.0;
        s=0.0;
        while(x/fi>(c/fi)+(x/(fi+f)))
        {
            s +=(double)c/fi;
            fi +=f;
        }
        s +=(double)x/fi;
        streamsize a=9.0;
        fileo<<"Case #"<<k<<": ";
        fileo<<s;
        fileo.precision(a);
        fileo<<endl;
    }
	return 0;
}
