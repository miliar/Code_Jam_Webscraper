#include<iostream>

using namespace std;

int main()
{
	int t,test,r1,r2,i,j,card1[4][4],card2[4][4],flag,val;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		flag=0;
		cin>>r1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>card1[i][j];

		cin>>r2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>card2[i][j];
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(card1[r1-1][i]==card2[r2-1][j])
				{
					flag++;
					val=card1[r1-1][i];
				}	
		if(flag==0)
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		else if(flag==1)
			cout<<"Case #"<<t<<": "<<val<<endl;
		else
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
	
	}	
}

