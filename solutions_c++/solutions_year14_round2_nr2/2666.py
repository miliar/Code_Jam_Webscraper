#include<iostream>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int a,b,k,c,m,i,j,answer;
	for(m=0;m<test;m++)
	{
		cin>>a;
		cin>>b;
		cin>>k;
		c=0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				answer=(i&j);
				if(answer<k)
				{
					c=c+1;
				}
			}
		}
		cout<<"Case #"<<m+1<<": "<<c<<endl;
	}
	return 0;
}
