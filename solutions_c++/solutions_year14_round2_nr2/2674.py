#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <cstring>
#include <cctype>
#include <deque>
using namespace std;
string converteBin(unsigned int n, unsigned int d)
{
    string v="";
    unsigned int x,y;
    while(n>0 || d>0)
    {
        x = n%2;
        n = n/2;
        y = d%2;
        d = d/2;
        if(x+y==2)v+=1+'0';
        else
            v+=0+'0';
    }
	string aux="";
	int t = v.size();
    return v;
}
unsigned int convertDec(string v)
{
    unsigned int acum=0;
    int tam = v.size();
    int el= tam-1;
    for(int i=tam-1;i>=0;i--)
    {
        if(v[i]!='0')
            acum+=pow(2,el);
        el--;
    }
    return acum;
}
int main()
{
int n;
unsigned int A,B,K;
int cont,caso=1;
cin>>n;
while(n>0)
{cont=0;
cin>>A>>B>>K;
int i,j;
unsigned int h;
for(i=0;i<A;i++)
{for(j=0;j<B;j++)
{
 h = convertDec(converteBin(i,j));
 if(h>=K)cont++;
}
}
cont = (A*B)-cont;
cout<<"Case #"<<caso<<": "<<cont<<endl;
caso++;
n--;}


return 0;
}