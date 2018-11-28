#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	int t=1,T;
	cin>>T;
	while(t<=T)
	{
		int a1,a2,ar1[4],ar2[4];
		int i,j;
		cin>>a1;
		int sim=0,num;
		i=0;
		while(i<4)
		{
			j=0;
			while(j<4)
			{
				cin>>num;
				if(i+1==a1)
					ar1[j]=num;
				j++;
			}
			i++;
		}
		cin>>a2;
		i=0;
		while(i<4)
		{
			j=0;
			while(j<4)
			{
				cin>>num;
				if(i+1==a2)
					ar2[j]=num;
				j++;
			}
			i++;
		}
		int id=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(ar1[i]==ar2[j])
				{
					id=ar1[i];
					sim++;
				}
		cout<<"Case #"<<t<<": ";
		if(sim==0)
			cout<<"Volunteer cheated!";
		else if(sim==1)
			cout<<id;
		else
			cout<<"Bad magician!";
		cout<<endl;
		t++;
	}
	return 0;
}
