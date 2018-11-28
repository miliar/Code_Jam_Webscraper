#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
bool com(int s)
{
	int data=s;
	int de=10;
	int left[14],right[14];
	int n=0;
	bool flag=true;
	while(1)
	{
        
		if(data/de==0) break;
		else
		{
			de*=10;
			n++;
		}
	}
		if(n==0) return true;
		
		for(int k=0;k<=n;k++)
		{
			right[k]=data%10;
			data/=10;
		}
		for(int k=0;k<=n/2;k++)
		{
			if(right[k]!=right[n-k]) {flag=false;break;}
		}
		return flag;
        
	    
}

int main()
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("outfile.out");
	int count;
	infile>>count;
	//cout<<count;
	for(int i=0;i<count;i++)
	{
		
		float MIN,MAX;
		int min,max;
		int number=0;
		infile>>min>>max;
		//cout<<endl<<min<<" " <<max<<endl;
		MIN=min*1.0;MAX=max*1.0;
        min=ceil(sqrt(MIN));
		max=floor(sqrt(MAX));
		//cout<<endl<<min<<" "<<max<<endl;

		for(int j=min;j<=max;j++)
		{
             if(com(j)&&com(j*j)) number++;
		}
		outfile<<"Case #"<<i+1<<": "<<number<<endl;
	}
}