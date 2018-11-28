#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;
#define ll long long int
int isPalin(ll n)
{
ll m=0,k=n;
while(n)
{
	m=m*10+ n%10;
	n=n/10;

}
//cout<<m<<endl;
if(m==k) {return 1;}
return 0;

}
int main()
{
	string s;
ifstream fin("input.txt");
ofstream fout("output.txt");
ll a,b,i,m,count,t=0;
fin>>s;
int test=1;
i=0;
while(s[i]!='\0')
	{t=t*10 + s[i]-'0';i++;}
cout<<t;

while(test<=t)
{
	fin >> a >> b;
	count=0;
	
	for(i=a;i<=(b);i++)
		{
			if(isPalin(i))
				{m=sqrt(i);
				if(m*m==i && isPalin(m))
					count++;
		        }

		}
		fout<<"Case #"<<test<<": "<<count<<"\n";
		test++;
}
}