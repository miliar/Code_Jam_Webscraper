#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

string generate_divisor(string X)
{
	string divisors;
	for(int b=2;b<=10;b++)
	{
		int number=0;
		int p=0;
		for(int i=X.size()-1;i>=0;i--)
		{
			int n=(int)(X[i]-'0');
			number+=n*pow(b,p++);
		}
		stringstream convert;
		convert << number ;
		string number_str=convert.str();
		divisors=divisors+number_str+" ";
	}
	return divisors;
}
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,j;
		scanf("%d %d",&n,&j);
		string jamcoin;
		string X;
		X="11";
		string divisors=generate_divisor(X);
		jamcoin=X;
		cout << "Case #1:\n";
		for(int i=1;i<=500;i++)
		{
			int num=i;
			for(int j=0;j<14;j++)
			{
				int mask=num&1;
				if(mask!=0)
					jamcoin+="11";
				else
					jamcoin+="00";
				num=num>>1;
			
			}
			jamcoin+=X;
			cout << jamcoin << " " << divisors <<endl;
			jamcoin.clear();
			jamcoin=X;
		}
		
	
	}
}