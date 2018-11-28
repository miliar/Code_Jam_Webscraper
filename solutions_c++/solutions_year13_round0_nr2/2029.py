#include <iostream>
using namespace std;
int arr[100][100],rm[100],cm[100];
int main()
{
	int t,n,m,tmp;
	cin>>t;
	for(int jj=1; jj<=t; jj++)
	{
		cin>>n>>m;
		for(int i=0; i<m; i++)
			cm[i] = 0;
		for(int i=0; i<n; i++)
		{
			rm[i]=0;
			for(int j=0; j<m; j++)
			{
				cin>>tmp;
				arr[i][j] = tmp;
				cm[j] = max(cm[j], tmp);
				rm[i] = max(rm[i], tmp);
			}
		}
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<m; j++)
			{
				if(arr[i][j] != rm[i] && arr[i][j] != cm[j])
				{
					cout<<"Case #"<<jj<<": NO\n";
					//cout<<i<<" "<<j<<" "<<arr[i][j]<<" "<<cm[j]<<" "<<rm[i]<<endl;
					goto lst;
				}	
			}
		}
		cout<<"Case #"<<jj<<": YES\n";
		lst:
		;		
	}
	return 0;
}	
