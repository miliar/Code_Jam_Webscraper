#include <iostream>
//#include <conio>

using namespace std;


int verify(int a[4][4],int ans,int b[4][4],int ans2);


int verify(int a[4][4],int ans,int b[4][4],int ans2)
{
	int count=0;
	int i,count1;	
	for(i=1;i<=4;i++)
		{ 
			for(int j=1;j<=4;j++)
				{
					if (a[ans][i]==b[ans2][j])
					{
						count1=a[ans][i];
						count++;
					}
				}
		}
		//cout<<count1<<endl;
		if(count==1)
		{
			return count1;
		}
		else if(count==0)
			return -1;
		else 
			return -2;
	}
int main()
{
	int q;
	cin>>q;
	int j;
	j=q;
	while(q!=0)
	{
	int a[4][4];
	int b[4][4];
	int ans=-1;
	int ans2=-1;
	cin>>ans;
	for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
				cin>>a[i][j];
		}
	cin>>ans2;
	
	for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
				cin>>b[i][j];
		}
	int s=verify(a,ans,b,ans2);
	if(s==-2)
	cout<<"Case #"<<j-q+1<<": Bad magician!"<<endl;
	else if(s==-1)
	cout<<"Case #"<<j-q+1<<": Volunteer cheated!"<<endl;
	else
	cout<<"Case #"<<j-q+1<<": "<<s<<endl;
	q--;
	}
}
	
