#include <iostream>
//#include <cstdio>
using namespace std;
int main()
{
	int test,n=0,i,j;
	int arr[4],dup,count,row;
	cin>>test;
	while(n!=test)
	{
		count=0;
		int hash[17]={0};
		cin>>row;
//		cout<<row<<endl;
		for(i=0;i<4;i++)
		{
			if(i==row-1)
			{
				for(j=0;j<4;j++)
				{
					cin>>arr[j];
					hash[arr[j]]=1;
//					cout<<arr[j]<<"\t";
				}
			}
			else
			{
				for(j=0;j<4;j++)
				{
					cin>>dup;
				}
			}

		}
		cin>>row;
//		cout<<endl<<row<<endl;
		for(i=0;i<4;i++)
		{
			if(i==row-1)
			{
				for(j=0;j<4;j++)
				{
					cin>>arr[j];
				//	cout<<arr[j]<<"\t";
					if(hash[arr[j]]==1)
					{
//						cout<<arr[j]<<"\t";
						hash[arr[j]]=2;
						count++;
					}
				}
			}
			else
			{
				for(j=0;j<4;j++)
				{
					cin>>dup;
				}
			}
		}
//		cout<<endl<<count<<endl;
		cout<<"case #"<<n+1<<": "; 
		if(count>1)
			cout<<"Bad magician!"<<endl;
		else if(count<1)
			cout<<"Volunteer cheated!"<<endl;
		else 
			{
				for(j=0;j<4;j++)
					if(hash[arr[j]]==2)
						cout<<arr[j]<<endl;
			}
			n++;
	}
}