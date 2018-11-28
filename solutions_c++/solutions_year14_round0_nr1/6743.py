#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,I;
	cin>>t;
	for(I=1;I<=t;I++)
	{
		int n,i,j;
		cin>>n;
		
		int A[4][4];
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>A[i][j];
		vector <int> check;
		for(i=0;i<4;i++)
			check.push_back(A[n-1][i]);
		cin>>n;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>A[i][j];
		
		int flag = 0;
		int pos = -1;
		for(i=0;i<4;i++)
		{	
			for(j=0;j<4;j++)
			{
				if(flag==0 && A[n-1][i] == check[j])
				{
					flag = 1;
					pos = j;
				}
				else if(flag==1 && A[n-1][i] == check[j])
					flag = 2;
			}
		}
		if(flag==0)
			cout<<"Case #"<<I<<": Volunteer cheated!\n";
		else if(flag==1)
			cout<<"Case #"<<I<<": "<<check[pos]<<endl;
		else
			cout<<"Case #"<<I<<": Bad magician!\n";
	}
	return 0;
}