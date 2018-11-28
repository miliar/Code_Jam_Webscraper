#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

int A,B;
int func();
int isperfectsquare(int i);
int ispalin(int i);

int main()
{
	int res;
	int T;
	fin>>T;
	int i=0;
	while(i<T)
	{
		fin>>A;
		fin>>B;
		res=func();
		
		i++;
		fout<<"Case #";
		fout<<i;
		fout<<": ";
		fout<<res;
		
		if(i!=T){fout<<"\n";}
	}
	return(0);
}

int func()
{

	int count=0;
	int i;
	int perfect;
	int ipalin;
	int perfectpalin;
	for(i=A;i<=B;i++)
	{
		perfect=isperfectsquare(i);
		if(perfect!=-1)
		{
			ipalin=ispalin(i);
			if(ipalin==1)
			{
				perfectpalin=ispalin(perfect);
				if(perfectpalin==1){count++;}
			}
		}
	}
	return(count);
}

int isperfectsquare(int i)
{
	int x=(int)sqrt(i);
	if((x*x)==i){return(x);}
	return(-1);
}

int ispalin(int i)
{
	int rev=0,rem;
	int x=i;
	while(x>0)
	{
		rem=x%10;
		rev=(rev*10)+rem;
		x=x/10;
	}

	if(rev==i){return(1);}
	return(0);
}
