#include<iostream>
using namespace std;
int main()
{
	int t,m,n,k;
	cin>>t;
	int l=1;
	for(l=1;l<=t;l++)
	{
		cin>>m>>n>>k;
		int x=(int)m&n;
		//cout<<"x: "<<x;
		long count=0;
		int i,j;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				int p=i&j;
				if(p<k)
				 count++;
			}
		}
		cout<<"Case #"<<l<<": "<<count<<endl;
	}
	return 0;
}
