#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
int main()
{
ofstream outf;
ifstream inf;
outf.open("output.txt");
inf.open("input.in");
int testc,maxshy,standp,friends,i,j;
char *c;//for input string
inf>>testc; // for number of test cases
for( i=0;i<testc;i++)
{
inf>>maxshy; // maximum level of shyness
c=(char*)malloc((maxshy+2)*sizeof(char));
inf>>c;
standp=0;
friends=0;
for( j=0;j<=maxshy;j++)
{
	if(j==0)
		standp=(c[j]-'0');

	else if(j>standp)
		{
			friends+=j-standp;
			standp=(c[j]-'0')+j;
		}
	else
		{
			standp+=(c[j]-'0');
		}
}
outf<<"Case #"<<i+1<<": "<<friends<<endl;

free(c);
}
outf.close();
inf.close();
return 0;
}
