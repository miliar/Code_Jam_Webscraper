#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int c=0;c<T;++c)
	{
		int n,m;
		cin>>n>>m;
		vector <int> rowMin(n,100),rowMax(n),colMin(m,100),colMax(m);
		vector <vector <int> > arr(n);
		for(int i=0;i<n;i++)
		{
			arr[i].resize(m);
			for(int j=0;j<m;++j)
			{
				cin>>arr[i][j];
				rowMin[i]=min(rowMin[i],arr[i][j]);
				rowMax[i]=max(rowMax[i],arr[i][j]);
				colMin[j]=min(colMin[j],arr[i][j]);
				colMax[j]=max(colMax[j],arr[i][j]);
			}
		}
		int overAllMax=*max_element(colMax.begin(),colMax.end());
		bool ans=1;
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<m;++j)
			{
				if(!(arr[i][j]==rowMax[i] or arr[i][j]==colMax[j]))
				{
					ans=0;
					i=n;
					j=m;
				}
			}
		}
		if(ans)
			cout<<"Case #"<<c+1<<": YES\n";
		else
			cout<<"Case #"<<c+1<<": NO\n";
	}
	return 0;
}