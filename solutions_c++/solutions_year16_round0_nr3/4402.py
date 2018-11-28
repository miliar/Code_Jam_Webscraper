#include<bits/stdc++.h>
using namespace std;

long long int isPrime(long long int val)
{
	for(long long int i=2;i<=sqrt(val);i++)
		if(val%i==0)
			return i;
			
	return -1;		
}
long long int power(long long int x, long long  int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}
int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("main.txt");
	outfile.open("thisisit.txt");
	
	long long int j=1;
	long long int result=0;
	
	outfile << "Case #1:" << endl;
	while(j<=16384&&result<50)
	{	
		label:
		long long int i=0;
		long long int factors[10]={0};
		string str;
		infile >> str;
		
		long long int value=0;
		long long int count=0;
	
		for(i=2;i<=10;i++)
			{	
				value=0;
				for(long long int k=15;k>=0;k--)
					{
						value=value+(str[15-k]-48)*power(i,k);
					}
	
				long long int res=isPrime(value);	
				if(res!=-1)
					factors[count++]=res;
				else
					{
						j++;
						goto label;
					}
			}
		result++;
		
		outfile << str << " ";
		for(i=0;i<9;i++)
			outfile << factors[i] << " ";
		outfile << endl;
		j++;
	}
	return 0;
	
}
