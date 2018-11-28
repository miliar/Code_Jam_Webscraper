#include<iostream>
#include<vector>
#include<conio.h>
#include<cstdlib>
#include<iomanip>
#include<cmath>
#include<string>
#include<fstream>
#include<algorithm>

using namespace std;
int pos(long d)
{
	int p=d;
	while(p>1)
	{
		if(p%2!=0)
		{
			return 1;
		}
		else
		p=p/2;
	}
	return 0;
}
int hcf(int firstNum, int secondNum)
{
     while (firstNum != 0 && secondNum != 0)
     {
         if (firstNum > secondNum)
         {
            firstNum %= secondNum;
         }
         else
         {
            secondNum %= firstNum;
         }
     }

     if (firstNum == 0)
     {
         return secondNum;
     }
     else
     {
         return firstNum;
     }
}
int main()
{
	ifstream inp("input.in");
	ofstream out("output.txt");
	if(!inp || !out)
	{
		return 100;
	}
	int cases;
	inp>>cases;
	for(int z=1;z<=cases;z++)
	{
		long n,d;
		char c;
		inp>>n>>c>>d;
	//	long long p=hcf(n,d);
	//	n=n/p;
	//	d=d/p;
		long n1=n;
		int j=0;
		if(n<d)
		for(j=1;j<=41;j++)
		{
			n=n*2;
			if(n>=d)
			{
				break;
			}
		}
		out<<"Case #"<<z<<": ";

		if(j==41 || pos(d))
		{
			out<<"impossible";
		}
		else
		{
			out<<j;
		}
			out<<endl;
		
	
	}
	return 0;
}

