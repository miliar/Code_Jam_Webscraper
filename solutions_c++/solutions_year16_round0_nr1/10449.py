#include<iostream>
#include<fstream>
using namespace std;
long int n,a,y;
int t,x;
int main()
{
	int r,s,i,p;
	x=1;
	ofstream myfile;
	myfile.open("output.txt");
	cin>>t;
	while(x<=t)
	{
		s=0;
		p=2;
		int ar[10]={0};
		cin>>n;
		a=n;
		if(n==0)
		{
			myfile<<"case #"<<x<<": INSOMNIA"<<"\n";
			x++;
			continue;
		}
		if(n>0)
		{
		while(s<=10)
		{
			while(n>0)
			{
				r=n%10;
				ar[r]=1;
				n=n/10;
			}
			for(i=0;i<=9;i++)
			{
				s=s+ar[i];
			}
			if(s==10)
			{
			    myfile<<"case #"<<x<<": "<<y<<"\n";	
			    break;
			}
			else
			{
			n=a*p;
			y=n;
			}p++;
			s=0;
		}
		}
		x++;
		}
		myfile.close();
	}


