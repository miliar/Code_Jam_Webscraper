#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

inline int palindrome(long long n)
{
	int a[100];
	int l,i,s,f;
	i=0;
	while(n!=0)
	{
		a[i]=n%10;
		n/=10;
		i++;
	}

	l=i;

	s=l/2;
	f=1;
	for(i=0;i<s;i++)
	{
		if(a[i]!=a[l-i-1])
		{
			f=0;
			break;
		}
	}

	return f;
}
int main()
{
	int t,i,num,si,ei,k;
	long long lookup[]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111,11111111,20000002};
	
	unsigned long long a,b,s,e,p;
	 long double stemp;
	ifstream fin("C:/a.txt");
	ofstream fout("C:/o.txt");
	fin>>t;
	
	for(k=0;k<t;k++)
	{
		fin>>a>>b;
		
		
		num=0;
	    /*short version
	   stemp=a;
		s=sqrt(stemp);
		e=s*s;
		if(e<a)
			s+=1;
		stemp=b;
		e=sqrt(stemp);

		do
		{
			
			
			if(palindrome(s)==1)
			{
			  a=s*s;
				if(palindrome(a)==1)
				{
				    fout<<s<<",";
					num++;
				}
			}
			
			s++;
		}while(s<=e);

		fout<<"Case #"<<(i+1)<<": "<<num<<endl;*/


		 //long version
		stemp=a;
		s=sqrt(stemp);
		if(s*s!=a)
			s++;
		stemp=b;
		e=sqrt(stemp);
		
		for(i=0;i<48;i++)
		{
			p=lookup[i];
			if(p>=s&&p<=e)
				num++;
			else if(p>e)
				break;
		}
		
		fout<<"Case #"<<(k+1)<<": "<<num<<endl;
		/********************/
	}

		
	return 0;
}