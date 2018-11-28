#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int arr1[4][4],arr2[4][4];
	int compare[4];
	int count;
	int cas =1;
	while(t--)
	{
		int ans1, ans2;
		count=0;
		
		cin>>ans1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr1[i][j];
			}
		}
		
		cin>>ans2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr2[i][j];
			}
		}
		
		for(int j=0;j<4;j++)
			{
				compare[j]=0;	
			}
			
		
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(arr1[ans1-1][i]==arr2[ans2-1][j])
				{
					compare[i]=1;
					count++;
				}	
			}
		}
		
		
		if(count==0){
				cout<<"Case #"<<cas<<": Volunteer cheated!"<<endl;
				cas++;}
				
		for(int i=0;i<4;i++)
		{
			if(compare[i]==1 && count==1)
				{
					cout<<"Case #"<<cas<<": "<<arr1[ans1-1][i]<<endl;
					cas++;
					break;
				}
		}
		
		for(int i=0;i<4;i++)
		{
			if(compare[i]=1 && count!=1 && count!=0)
				{
					cout<<"Case #"<<cas<<": Bad magician!"<<endl;
					cas++;
					break;
				}
		}
		
	}
	return 0;
}