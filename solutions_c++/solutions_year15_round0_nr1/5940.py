#include<iostream>
using namespace std;
int main()
{
	long long int t;
	cin >>t;
	long long int bbb[t];
	for (int x=0;x<t;x++)
	{
		long long int n;
		cin >>n;
		long long int sum=0,asum=0;
		char aaa[n+1];
		for (int i=0;i<n+1;i++)
		    cin >>aaa[i];
		for (int i=0;i<n;i++)
		{
			asum+=aaa[i]-48;
			if (asum+sum>=i+1)      sum+=0;
			else if (asum+sum<i+1)  sum+=i+1-asum-sum;
		}
		bbb[x]=sum;
	}
	for (int y=0;y<t;y++)
	    cout <<"Case #"<<y+1<<": "<<bbb[y]<<"\n";
	system ("pause");
    return 0;
}
