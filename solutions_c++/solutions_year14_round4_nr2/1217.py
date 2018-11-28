#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
struct pr
{
	int x,idx;
};
int main()
{
	freopen("Bin.in","r",stdin);
	freopen("Bout.txt","w",stdout);
	int T;
	cin>>T;
	for(int x=0;x<T;x++)
	{
		int N;
		cin>>N;
		int ar[N],arr[N];
		for(int i=0;i<N;i++)
		{
			cin>>ar[i];
			arr[i]=ar[i];
		}
		long long ans=0;
		/*for(int i=0;i<mxps;i++)
			for(int j=mxps-1;j>i;j--)
				if(ar[j]<ar[j-1])
				{
					int tmp=ar[j-1];
					ar[j-1]=ar[j];
					ar[j]=tmp;
					ans++;
				}
		for(int i=mxps+1;i<N;i++)
			for(int j=N-1;j>i;j--)
				if(ar[j]>ar[j-1])
				{
					int tmp=ar[j-1];
					ar[j-1]=ar[j];
					ar[j]=tmp;
					ans++;
				}*/
		sort(ar,ar+N);
		//cout<<ar[0]<<endl;
		int L=0,R=N-1;
		for(int i=0,k;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(arr[j]==ar[i])
				{
					k=j;
					break;
				}
			}
			if((k-L)<(R-k))
			{
				for(int j=k,tmp;j>L;j--)
				{
					tmp=arr[j],arr[j]=arr[j-1],arr[j-1]=tmp;
					ans++;
				}
				L++;
			}
			else
			{
				for(int j=k,tmp;j<R;j++)
				{
					tmp=arr[j],arr[j]=arr[j+1],arr[j+1]=tmp;
					ans++;
				}
				R--;
			}
		}
		printf("Case #%d: ",x+1);
		cout<<ans<<endl;
		//for(int i=0;i<N;i++)
		//	cout<<arr[i]<<endl;
	}
	return 0;
}
