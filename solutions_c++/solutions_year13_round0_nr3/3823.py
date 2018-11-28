#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>
#pragma comment(linker, "/STACK:10000000") 
#define md 1000000007

using namespace std;

int ans,aa,bb,test,t,i;
long long a[20];


int main()
{
ifstream f("input.txt");
ofstream g("output.txt");
a[1]=1;
a[2]=121;
a[3]=4;
a[4]=9;
a[5]=484;
a[6]=12321;
a[7]=1234321;
a[8]=14641;
a[9]=44944;
a[10]=121242121;
a[11]=123454321;
a[12]=12345654321;
a[13]=125686521;
a[14]=1212225222121;
a[15]=1214428244121;
a[16]=1232346432321;
a[17]=1234567654321;
a[18]=123456787654321;
f>>t;
for (test=1;test<=t;test++)
{
	f>>aa>>bb;
	ans=0;
	for (i=1;i<=18;i++) if (a[i]>=aa && a[i]<=bb) ans++;
	g<<"Case #"<<test<<": "<<ans<<endl;
	
}	
}
