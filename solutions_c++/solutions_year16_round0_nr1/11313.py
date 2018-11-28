#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int insomnia( int n)
{
	 int temp;
	int a[10];
	int digit,i,j,ins;

	
	for(i=0;i<10;i++)
	{
		a[i] = -1;
	}
	for(i=1;i<=100000;i++)
	{
		bool flag = true;
		temp = n*i;
		ins = n*i;
		while(temp>0)
		{
			digit = temp%10;
			temp = temp/10;
			a[digit] = digit;
		}
		
		for(j=0;j<10;j++)
		{
			if(a[j]!=j)
			{
			   flag = false;
			}
		}
		
		if(flag)
		{
			return ins;
	    }	 
	
	}
	
		return -1;
	
}

int main()
{   
	int tc,i,res;
    int n;
	cin>>tc;
	string b[tc];
	for(i=0;i<tc;i++)
	{
		cin>>n;
	    res	= insomnia(n);
	    if(res==-1)
	     {
		 b[i] = "INSOMNIA";
	 }
	else
	{   
		string result;
		ostringstream convert;
		convert << res;
		
		 b[i] = convert.str() ; 
}
}

for(i=1;i<=tc;i++)
{
	cout <<"Case #"<<i<<": "<<b[i-1]<<endl;
}
	    
}