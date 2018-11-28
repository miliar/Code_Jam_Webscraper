#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int t1=1;
	while(t1<=t)
	{
		int ans1;
		cin>>ans1;
		int y[20]={0};
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{	int a;
				cin>>a;
				if(ans1==i)
				y[a]=1;
				    
			}
		}
		int ans2;
		cin>>ans2;
		int flag=0;
		int num;
		
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{	int a;
				cin>>a;
				if(ans2==i)
				{
					if(y[a]==1)
					{
					flag++;
					num=a;
					}
				}
			}
		}
		
		if(flag==1)
		cout<<"Case #"<<t1<<": "<<num;
		else if(flag>1)
		cout<<"Case #"<<t1<<": Bad magician!";
		else 
		cout<<"Case #"<<t1<<": Volunteer cheated!";
	cout<<"\n";

		t1++;
		
	}
	
	
	
	return 0;
}