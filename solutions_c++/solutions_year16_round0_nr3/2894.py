#include <bits/stdc++.h>
using namespace std;
bool arr[40];
int main()
{
    int t;cin>>t;
	while(t--)
	{
		cout<<"Case #1:\n";
		int n,j1;cin>>n>>j1;
		int cnt=0;
		int start=4;int start1=6;
		while(cnt<450)
		{
			
			if(cnt==0)
			{
//				cout<<"@";
				int i=2;
				arr[n-1]=arr[n-2]=arr[1]=arr[0]=1;
				while(i<n-3)
				{
					arr[i+1]=true;arr[i]=true;
					for(int j=n-1;j>=0;j--)
					cout<<arr[j];
					cout<<" ";
					for(int k=2;k<=10;k++)
					cout<<k+1<<" ";
					arr[i+1]=arr[i]=false;
					cnt++;i++;
					cout<<"\n";
				}
			}
			else if(cnt<352)
			{
				int x=start,y=2;
				arr[n-1]=arr[n-2]=arr[1]=arr[0]=1;
				while(x<n-3)
				{
				   arr[x+1]=arr[x]	=arr[y+1]=arr[y]=1;
				   for(int j=n-1;j>=0;j--)
					cout<<arr[j];
					cout<<" ";
					for(int k=2;k<=10;k++)
					cout<<k+1<<" ";
					arr[x+1]=arr[x]	=arr[y+1]=arr[y]=0;
					cnt++;
					cout<<"\n";
					x++;y++;
				}
				start++;
			}
//			cout<<cnt<<"\n";
		   else 
		   {
		   	   arr[n-1]=arr[n-2]=arr[2]=arr[1]=arr[0]=1;
		   	   int x=start1,y=4;
		   	    while(x<n-3)
				{
				   arr[x+1]=arr[x]	=arr[y+1]=arr[y]=1;
				   for(int j=n-1;j>=0;j--)
					cout<<arr[j];
					cout<<" ";
					for(int k=2;k<=10;k++)
					cout<<k+1<<" ";
					arr[x+1]=arr[x]	=arr[y+1]=arr[y]=0;
					cnt++;
					cout<<"\n";
					x++;y++;
				}
				start1++;
		   }	
		}
	}	
}
