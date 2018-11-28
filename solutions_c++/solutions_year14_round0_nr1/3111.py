#include<iostream>
using namespace std;
//------------------------------------------------------

int main()
{
	freopen("k1.txt","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int n;
		cin>>n;
		int arr[5];
		int temp;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>temp;
				if(i+1==n)
				{
					arr[j]=temp;
				}
			}
		}
		
		cin>>n;
		int count=0,number;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>temp;
				if(i+1==n)
				{
					for(int k=0;k<4;k++)
					{
						if(arr[k]==temp)
						{
							count++;
							number=temp;
						}
					}
				}
			}
		}
		if(count==1)
			cout<<"Case #"<<test<<": "<<number<<endl;
		else if(count==0)
			cout<<"Case #"<<test<<": Volunteer cheated!\n";
 		else
			cout<<"Case #"<<test<<": Bad magician!\n";
	}
}
