#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t,i,j,n,count,res;
	char inp[1005];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		count=0;
		res=0;
		for(j=0;j<=n;j++)
		{
			cin>>inp[j];
		}
		count+=inp[0]-'0';
		//cout<<"counting :"<<count<<"\n";
		for(j=1;j<=n;j++)
		{
			if(count<j)
			{
				res+=j-count;
				count+=j-count;
			}
		//		cout<<"counting 1 :"<<count<<"\n";
			count+=inp[j]-'0';
		//		cout<<"counting 2 :"<<count<<"\n";
		}
		cout<<"Case #"<<i+1<<": "<<res<<"\n";
	}
	cin>>n;
	return 0;
}
