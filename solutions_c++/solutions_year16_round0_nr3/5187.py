#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,T;
	int n,j;
	cin>>t;
	T=t;
	while(t--)
	{
		cin>>n>>j;
		cout<<"Case #"<<T-t<<":"<<endl;
		int arr[35];
		for(int i=0;i<32;i++)
		{
			arr[i]=i;
		}
		int arr1[5]={6,5,4,3,2};
		int mul1[2]={7,0};
		for(int i=0;i<32;i++)
		{
			int res[16]={0};
			int arr12[7]={8,-1,-1,-1,-1,-1,0};
			int ans[5]={-1,-1,-1,-1,-1};
			for(int j=4;j>=0;j--)
			{
				if(arr[i]&1)
				{
					ans[j]=arr1[j];
				}
				arr[i]=arr[i]>>1;
				//cout<<arr[i]<<endl;
			}
			for(int j=1;j<6;j++)
			{
				arr12[j]=ans[j-1];
			}
			for(int k=0;k<2;k++)
			{
				for(int j=0;j<7;j++)
				{
					if(arr12[j]>=0)
					{
						res[arr12[j]+mul1[k]]=1;
					}
				}
			}
			for(int j=15;j>=0;j--)
			{
				cout<<res[j];
			}
			for(int k=2;k<=10;k++)
			{
				int xx=pow(k,7);
				xx++;
				cout<<" "<<xx;
			}
			cout<<endl;
		}
		for(int i=0;i<16;i++)
		{
			arr[i]=i;
		}
		int arr11[4]={8,7,5,4};
		mul1[0]--;
		for(int i=0;i<16;i++)
		{
			int res[16]={0};
			int arr12[6]={9,-1,-1,-1,-1,0};
			int ans[4]={-1,-1,-1,-1};
			for(int j=3;j>=0;j--)
			{
				if(arr[i]&1)
				{
					ans[j]=arr11[j];
				}
				arr[i]=arr[i]>>1;
				//cout<<arr[i]<<endl;
			}
			for(int j=1;j<5;j++)
			{
				arr12[j]=ans[j-1];
			}
			//for(int j=0;j<6;j++)
//			{
//				cout<<endl<<arr12[j]<<" ";
//			}
//			cout<<endl;
			for(int k=0;k<2;k++)
			{
				for(int j=0;j<6;j++)
				{
					if(arr12[j]>=0)
					{
						res[arr12[j]+mul1[k]]=1;
					}
				}
			}
			for(int j=15;j>=0;j--)
			{
				cout<<res[j];
			}
			for(int k=2;k<=10;k++)
			{
				int xx=pow(k,6);
				xx++;
				cout<<" "<<xx;
			}
			cout<<endl;
			
		}
		cout<<"1111111111111111 3 4 5 6 7 8 9 10 11"<<endl;
		cout<<"1100000000000011 3 4 5 6 7 8 9 10 11"<<endl;
	}
	return 0;
}
