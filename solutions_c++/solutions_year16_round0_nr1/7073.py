#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	long long int t=0,n=0,i=0,j=0,k=0,temp1=0,temp2=0;
	ifstream input;
	input.open("quest.in");
	ofstream output;
	output.open("answer.in");
	input>>t;
	int a[10];
	for(k=0;k<t;k++)
	{
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		input>>n;
		if(n==0)
		{
			output<<"Case #"<<k+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		temp1=n;
		i=0;
		while(i<10)
		{
			temp2=n;
			i=0;
			do
			{
				a[temp2%10]=1;
				temp2/=10;
			}while(temp2);
			i=0;
			while(a[i]&&i<10)
			{
				i++;
			}
			//output<<" i = "<<i;
			n+=temp1;
		}
		output<<"Case #"<<k+1<<": "<<n-temp1<<endl;						
	}
	return 0;
}
