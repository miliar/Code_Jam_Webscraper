#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t,temp2,count=0,flag1[10]={},tt=0;
	long long int n,temp1,r;
  	ifstream infile ("A-large.in");
  	ofstream outfile("output1.out");
  	infile>>t;
	while(t--)
	{
		for(int j=0;j<10;j++)
			flag1[j]=0;
	  	infile>>n;
	  	if(n==0)
	  	{
			outfile<<"Case #"<<++tt<<": INSOMNIA"<<endl;	
			continue;
	  	}
		for(int i=1;;i++)
		{
			temp1=n*i;
			r=temp1;
			while(temp1!=0)
			{
				temp2=temp1%10;
				temp1/=10;
				flag1[temp2]=1;
			}
			count=0;
			for(int j=0;j<10;j++)
				if(flag1[j]==1)
					count++;
			if(count==10)
			{
				outfile<<"Case #"<<++tt<<": "<<r<<endl;
				break;
			}
				
		}				
	}
	return 0;
}




