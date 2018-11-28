#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int m;
	cin>>m;
	int mm=m;
	int N,M;
	int arr[105][105];
	int mj[105];
	int mi[105];
	while(m--)
	{
		string res="YES";
		cin>>N>>M;
		memset(mi,0,sizeof(mi));
		memset(mj,0,sizeof(mj));
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				{
					cin>>arr[i][j];
					if(arr[i][j]>mi[i])mi[i]=arr[i][j];
					if(arr[i][j]>mj[j])mj[j]=arr[i][j];
			}
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				if(arr[i][j]<mi[i] && arr[i][j]<mj[j])res="NO";
		cout<<"Case #"<<(mm-m)<<": "<<res<<endl;
	}
	return 0;
}