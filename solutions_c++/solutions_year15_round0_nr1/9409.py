using namespace std;
#include <iostream>
int main()
{
	
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int smax;
		cin>>smax;
		smax++;
		char shy[smax];
		cin>>shy;
		int result=0,sum=0;
		for(int i=0;i<smax;i++)
		{
			shy[i]=shy[i]-48;
		}
		for(int i=0;i<smax;i++)
		{
			if(sum<i)
			{
				result=result+(i-sum);
				shy[i]=shy[i]+(i-sum);
			}
			sum=sum+shy[i];
		}
		cout<<"Case #"<<k+1<<": "<<result<<"\n";
	}
	
	return 0;
}
