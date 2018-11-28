#include <iostream>
using namespace std;

int main()
{
	int t,r1,r2,n,r;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>r;
		int a[17]={0};
		int y=1;
		while(y<=4)
		{
			for(int i=1;i<=4;i++)
			{
			cin>>n;
			if(y==r) a[n]++;	
			}
			y++;
		}
		cin>>r;
		y=1;
		while(y<=4)
		{
			for(int i=1;i<=4;i++)
			{
			cin>>n;
			if(y==r) a[n]++;	
			}
			y++;
		}
		int res;int c2=0;
		for(int i=1;i<17;i++)
		{
			if(a[i]==2) {
				res=i; c2++;
			}	
		}
		if(c2==0) cout<<"Case #"<<i<<": Volunteer cheated!\n";
		else if (c2>1) cout<<"Case #"<<i<<": Bad magician!\n";
		else cout<<"Case #"<<i<<": "<<res<<"\n";
}
return 0;
}
