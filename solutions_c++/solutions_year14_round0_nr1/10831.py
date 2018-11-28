#include<iostream>
using namespace std;
struct in
{
	int x;
	int y;
	int temp[4];
	int temp1[4];
};

int main()
{
	int card[4][4],test,u=0,count,ans;
	
cin>>test;
in* a=new in[test];

while(u!=test)
{
	
	cin>>a[u].x;		
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++){
		
		cin>>card[i][j];
		if(i==a[u].x-1)
		a[u].temp[j]=card[i][j];
	}
	}
	
	cin>>a[u].y;
	
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++){
		
		cin>>card[i][j];
		if(i==a[u].y-1)
		a[u].temp1[j]=card[i][j];
	}
	}

u++;
}
u=0;

while(u!=test)
{
	
	count=0;
	ans=0;
	
for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++){
		if(a[u].temp[i]==a[u].temp1[j])
		{
			count++;
			ans=a[u].temp[i];
		}		
	}
}
	if(count==0)
	cout<<"Case #"<<u+1<<": Volunteer cheated!";
	else if(count<=4&&count>1)
	cout<<"Case #"<<u+1<<": Bad magician!";
	else if(count==1)	
	cout<<"Case #"<<u+1<<": "<<ans;
u++;
cout<<endl;	
}
	 return 0;
}


