//Standing Ovation problem.
#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
	int max_shy,test;
	//cout<<"Enter the no. of test cases";
	cin>>test;
	int friends[test];
	for(int k=0;k<test;k++)
	{
		//cout<<"\nEnter the shyness level of the shyest person in the audience :";
		cin>>max_shy;
		string shyness1;
		int shyness[max_shy+1];
		//cout<<"\nEnter the no. of shy people corresponding to the shyness :";
		cin>>shyness1;
		friends[k]=0;
		for(int i=0;i<=max_shy;i++)
		shyness[i]=shyness1[i]-'0';
		int key=0,sum;
		key=shyness[0];
		sum=key;
		if(sum==0)
		friends[k]++;
		sum=sum+friends[k];
		for(int i=1;i<=max_shy;i++)
		{
			key=shyness[i];
			if(i>sum )
			{
				friends[k]++;
				sum++;
			}
			sum=sum+key;
		}
		
	}
	for(int k=0;k<test;k++)
	{
		cout<<"Case #"<<k+1<<": "<<friends[k]<<endl;
	}
	return 0;
}
