#include<iostream>
#include<math.h>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	int s, T;
	long long int n;
	ifstream in("A-large.in");
//	cout<<"enter the number of test cases";
//	cin>>T;
if(!in)
{
	cout<<"error";
}
in>>s;
T=s;
	for(int i=1;i<=T;i++)
	{
//		cout<<"enter the numeber";
//		cin>>n;
in>>n;
		int count=0,arr[10];
		for(int j=0;j<10;j++)
		{
			arr[j]=0;
		}
		int c=1;
		while(count!=10)
		{
			
			int t,x;
			x=t=n*c;
			while(t!=0)
			{
			
			int r=t%10;
		//	cout<<r;
			t=t/10;
		//	cout<<t;
			if(arr[r]==0)
			{
				arr[r]=1;
				count++;
			}
		}
		
		//count++;
		ofstream out;
		out.open("output2",ios::app);
		
		if(count==10)
		{
			out<<"Case"<<" "<<"#"<<i<<":"<<" "<<x<<endl;
		}
		if(n==0)
		{
			out<<"Case"<<" "<<"#"<<i<<":"<<" "<<"INSOMNIA"<<endl;
			break;
		}
		c++;
		out.close();
		
		}
	}
	in.close();
	return 0;
}
