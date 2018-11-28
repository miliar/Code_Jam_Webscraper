// Fair and Square.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<fstream>
#include<math.h>
#include<conio.h>
using namespace std;

struct testcase
{
	int a,b;
	//bool fnsqno;
};
bool isPalindrome(int n)
{
	int original=n;
	int temp=n;
	int reversed=0;
	int i=0;
	while(temp>0)
	{
		temp=temp/10;
		i++;
	}
	int j=1;
	while(n>0)
	{
		int num=n%((int)(pow((float)10,1)));
		reversed = reversed + pow((float)10,i-j)*num;
		n=n/(pow((float)10,1));
		j++;

	}
	if(reversed==original)
	{
		return true;
	}
	else
	{
		return false;
	}
}
int main()
{
	
	int numtc=0;
	ifstream inf("nam.txt");
	ofstream outf("otp.txt");
	inf>>numtc;
	testcase *tc=new testcase[numtc];
	for(int i=0;i<numtc;i++)
	{
		inf>>tc[i].a;
		inf>>tc[i].b;
	}
	
	for(int i=0;i<numtc;i++)
	{
		int numFairNSq=0;
		for(int j=tc[i].a;j<=tc[i].b;j++)
		{
			bool fair=isPalindrome(j);
			float sqroot1=sqrt((float)j);
			float sqroot2=floor(sqroot1);
			if(sqroot1==sqroot2 && true==fair)
			{
				if(true==isPalindrome((int)sqroot1))
				{
					numFairNSq++;
				}
				
			}
		}
		outf<<"Case #"<<i+1<<": "<<numFairNSq<<endl;
	}
	return 0;
}

