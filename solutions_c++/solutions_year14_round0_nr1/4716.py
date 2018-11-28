#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
			int a[4],b[4],c2;
		cin>>n;
		for(int j=1;j<=n;j++)
		{
					for(int j=0;j<4;j++){cin>>a[j];}
		}
	for(int p=n;p<4;p++)
		{
			for(int j=0;j<4;j++)cin>>c2;
		}
		
	//	for(int j=0;j<4;j++)cout<<a[j]<<" ";
		
		cin>>n;
		for(int j=1;j<=n;j++)
		{
					for(int j=0;j<4;j++){cin>>b[j];}
		}
		
		
		
		for(int p=n;p<4;p++)
		{
			for(int j=0;j<4;j++)cin>>c2;
		}
	
		int c,counter=0;
	for(int q=0;q<4;q++)
	{
		for(int w=0;w<4;w++)
		{
			if(a[q]==b[w]) {c=a[q];counter++;}
	}
}
 if(counter==1) cout<<"Case #"<<i+1<<": "<<c<<endl;
 if(counter==0) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
 if(counter>1) cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
	}
}
