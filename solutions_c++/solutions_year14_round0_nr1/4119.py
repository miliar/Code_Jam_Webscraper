#include<fstream>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	
	cin.open("yoyoinp.txt");
	cout.open("output.txt");
	int t,i,j,count,I,n,x,temp;
	int a[5],b[5];
	
	cin>>t;
	
	for(I=1;I<=t;I++)
	{
		cin>>n;
		
		for(i=1;i<=4;i++)
		{
			if(i==n)
			{
				for(j=1;j<=4;j++)
				{
					cin>>a[j];
				}
				
			}
			else
			{
				for(j=1;j<=4;j++)
				cin>>temp;
			}
		}
		
				cin>>n;
		
		for(i=1;i<=4;i++)
		{
			if(i==n)
			{
				for(j=1;j<=4;j++)
				{
					cin>>b[j];
				}
				
			}
			else
			{
				for(j=1;j<=4;j++)
				cin>>temp;
			}
		}
		
		count=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(a[i]==b[j])
				{
				x=a[i];
				count++;
				}
			}
		}
		if(count==1)
		{
			cout<<"Case #"<<I<<": "<<x<<endl;
		}
		else if(count>1)
		{
			cout<<"Case #"<<I<<": Bad magician!\n";
		}
		else if(count==0)
		{
			cout<<"Case #"<<I<<": Volunteer cheated!\n";
		}
		
		
	}
	
	cin.close();
	cout.close();
	return 0;
	
}