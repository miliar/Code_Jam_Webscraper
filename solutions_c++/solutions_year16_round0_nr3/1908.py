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
		int arr[1000];
		for(int i=0;i<501;i++)
		{
			arr[i]=i;
		}
		int arr1[13]={14,13,12,11,10,9,8,7,6,5,4,3,2};
		int mul1[2]={15,0};
		for(int i=0;i<500;i++)
		{
			int res[32]={0};
			int arr12[15]={16,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0};
			int ans[13]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
			for(int j=12;j>=0;j--)
			{
				if(arr[i]&1)
				{
					ans[j]=arr1[j];
				}
				arr[i]=arr[i]>>1;
				//cout<<arr[i]<<endl;
			}
			for(int j=1;j<14;j++)
			{
				arr12[j]=ans[j-1];
			}
			for(int k=0;k<2;k++)
			{
				for(int j=0;j<15;j++)
				{
					if(arr12[j]>=0)
					{
						res[arr12[j]+mul1[k]]=1;
					}
				}
			}
			for(int j=31;j>=0;j--)
			{
				cout<<res[j];
			}
			for(int k=2;k<=10;k++)
			{
				long long int xx=pow(k,15);
				xx++;
				cout<<" "<<xx;
			}
			cout<<endl;
		}
	}
	return 0;
}
