#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int t;
	int data[100];
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int a;
		int n;
		cin>>a>>n;
		for(int i=0;i<n;i++)
			cin>>data[i];
		sort(data,data+n);
		int minop=101;
		if(a==1)
		{
			cout<<"Case #"<<k<<": "<<n<<"\n";
			continue;
		}
		for(int i=n;i>=0;i--)
		{
			int tempop=0;
			tempop=n-i;
			int tempa=a;
			
			for(int j=0;j<i;j++)
			{

				while(tempa<=data[j])
				{
					tempa+=tempa-1;
					tempop++;
					if(tempop>n)
						break;
				}
				if(tempop>n)
						break;
				tempa+=data[j];
			}
			if(minop>tempop)
				minop=tempop;
		}
		cout<<"Case #"<<k<<": "<<minop<<"\n";
	}
	return 0;
}