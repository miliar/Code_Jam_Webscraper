#include <bits/stdc++.h>
using namespace std;
int visited[10100];
vector<double> N,K;
int main()
{
	int TestCases;
	cin>>TestCases;
	for(int t = 1;t<=TestCases;t++)
	{
		int S = 0;
		memset(visited,false,sizeof(visited));
		cout<<"Case #"<<t<<": ";
		int n;
		cin>>n;
		N.clear();
		K.clear();
		N.resize(n);
		K.resize(n);
		for(int i = 0;i<n;i++)
			cin>>N[i];
		for(int i = 0;i<n;i++)
			cin>>K[i];
		sort(N.begin(),N.end());
		sort(K.begin(),K.end());
		for(int i = 0;i<n;i++)
		{
			for(int j = 0;j<n;j++)
			{
				if(K[i]<N[j]&&!visited[j])
				{
					S+=1;
					visited[j] = true;
					break;
				}
			}
		}
		cout<<S<<" ";
		S = 0;
		memset(visited,false,sizeof(visited));
		for(int i = 0;i<n;i++)
		{
			for(int j = 0;j<n;j++)
			{
				if(K[j]>N[i]&&!visited[j])
				{
					S+=1;
					visited[j] = true;
					break;
				}
			}
		}
		cout<<n - S<<endl;
	}
	return 0;
}
