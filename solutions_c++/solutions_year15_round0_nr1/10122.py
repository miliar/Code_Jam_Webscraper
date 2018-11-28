#include<iostream>
#include<cmath>
using namespace std;
int main()
{	int t, i, smax, j, sum=0, needed=0;
	long long si, s, p;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>smax;
		cin>>si;
		
		for(j=0;j<=smax;j++)
		{	p=pow(10.0,smax-j);
			s=si/p;
			si=si%p;			
			if(s==0)
			continue;
			if(sum<j)
			{
				needed+=j-sum;
				sum+=needed;
			}
			if(sum>=j)
			{
				sum=sum+s;
			}
		}
		cout<<"Case #"<<i+1<<": "<<needed<<endl;
		sum=0; needed=0;
	}
	return 0;
}
