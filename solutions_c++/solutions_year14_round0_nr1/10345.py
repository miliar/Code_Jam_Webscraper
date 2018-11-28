#include <iostream>
#include<algorithm>
#include<math.h>
using namespace std;

int main() {
	int t,r1,r2,i,j,a[4],b[4],count,ans,x,k=1;
	cin>>t;
	while(t--)
	{
		//cout<<t;
		cin>>r1;
		for(i=0;i<=3;i++)
			for(j=0;j<=3;j++)
			{
				if(i==r1-1)
				cin>>a[j];
				else
				cin>>x;
			}
		cin>>r2;
		for(i=0;i<=3;i++)
			for(j=0;j<=3;j++){
			if(i==r2-1)
				cin>>b[j];
				else cin>>x;}
				
		count=0;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		if(a[i]==b[j])
		{
			count++;
			ans=a[i];
		}
		if(count==0)
		cout<<"Case #"<<k++<<": "<<"Volunteer cheated!\n";
		else if(count==1)
		cout<<"Case #"<<k++<<": "<<ans<<"\n";
		else
		cout<<"Case #"<<k++<<": "<<"Bad magician!\n";
	}
	return 0;
}