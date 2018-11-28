#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int A[1010];

int main()
{
	int z;
	cin>>z;
	for(int v=0;v<z;v++)
	{
		int n;
		cin>>n;
		for(int i=0;i<=n;i++)
		{
			char a;
			cin>>a;
			A[i]=a-'0';
		}
		int mam=A[0];
		int ile=0;
		for(int i=1;i<=n;i++)
		{
			if(mam<i)
			{
				mam++;
				ile++;
			}
			mam+=A[i];
		}
		cout<<"Case #"<<v+1<<": "<<ile<<endl;
	}
}
