#include <iostream>
#include <string>
#include <vector>
#include <conio.h> 
#include <sstream> 
#include<fstream>
using namespace std;

int main() {
	ifstream fin("A-small-attempt7.in");
	ofstream fout("output1.txt");


	int n;
		int pll=1;
		int count2=1;
		int kl;
	fin>>kl;

	fin>>n;
    int ar[100];
	int c1=0,c2=1,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0;
	bool count=10;
	int i=0;
	int l=1;
	int k=0;
	int b=n;
	int c=n;
	while(kl>=1)
	{

	while(count>0)
	{
	
		 int pk;
		 k=n;
		 pk=k;
	do
	{
	ar[i]=k%10;
	k=k/10;
	i++;
	}while(k>0);
	for(int j=0;j<i;j++)
	{
		if(ar[j]==0)
		c1=1;
		else if(ar[j]==1)
			c2=1;
			else if(ar[j]==2)
			c3=1;
			else if(ar[j]==3)
			c4=1;
				else if(ar[j]==4)
			c5=1;
				else if(ar[j]==5)
			c6=1;
					else if(ar[j]==6)
			c7=1;
					else if(ar[j]==7)
			c8=1;
						else if(ar[j]==8)
			c9=1;
						else if(ar[j]==9)
			c10=1;
			
									if(c1==1&& c2==1&& c3==1&& c4==1&& c5==1&& c6==1&& c7==1&& c8==1&& c9==1&& c10==1)
	{
	
		count=0;
	}
	

	}
	i=0;

	l++;
	n=l*b;
	if(n==c || n==pk)
	{
		
		count2=0;
		break;
	}


	}
	if(count2==0)
	{
		fout<<"Case #"<<pll<<": INSOMNIA"<<endl;
		count2=1;
	}
	else
	{
	n=n-b;
   
fout<<"Case #"<<pll<<": "<<n<<endl;
	}
	fin>>n;
	pll++;
 c1=0,c2=1,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0;
	 count=10;
	 i=0;
	 l=1;
 k=0;
	 b=n;
	 c=n;
	
	kl--;
	}
	
	
}