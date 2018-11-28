#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		int N;
		cin>>N;int s=0;
		int arr[300]={0};
		for(int j=0;j<N;j++)
		{
			cin>>arr[j];
			s=s+arr[j];
		}
		if(N>2)
		{
			while(s!=0)
			{
				int max=0,mp=0;
				for(int k=0;k<N;k++)
				{
					if(max<arr[k])
					{
						max=arr[k];
						mp=k;
					}
				}
				if(s!=2)
				{cout<<(char)(mp+65)<<" ";

				arr[mp]--;
				s--;}
				else
				{
					for(int u=0;u<N;u++)
					{
						if(arr[u]!=0)
							cout<<(char)(u+65);
					}
					cout<<" ";
					s=s-2;
					break;
				}
				

			}
		}
		else if(N==2)
		{
			while(s!=0)
			{
				if(arr[0]>arr[1])
				{
					cout<<(char)(65)<<" ";
					arr[0]--;
					s--;
				}
				else if(arr[1]>arr[0])
				{
					cout<<(char)(66)<<" ";
					arr[1]--;
					s--;
				}
				else
				{
					for(int h=0;h<arr[0];h++)
					{
						cout<<"AB"<<" ";
						s=s-2;
					}
					break;

				}
			}
					


			
		}
		cout<<"\n";

	}
}