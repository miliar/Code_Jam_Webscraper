#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int T, N[50];

bool search(int a[50][20][20], int k, int I, int J, int S)
{
	for(int i = 0; i < 2*N[S] - 1; i++)
	{
		for(int j = 0; j < N[S]; j++)
		{
			if(i==I && j==J)
				continue;
			if(a[S][i][j] == k)
			{
				a[S][I][J] = -1;
				a[S][i][j] = -1;
				return true;
			}
					
		}
	}
	
	return false;
}



int main()
{
	
	int ls[50][20][20];
	vector<int> nu;
	int curr, I, J;
	cin>>T;
	for(int i = 0; i < T; i++)
	{
		cin>>N[i];
		for(int j = 0; j < 2*N[i] - 1; j++)
		{
			for(int k = 0; k < N[i]; k++)
				cin>>ls[i][j][k];
		}
		
		
	}
	for(int l = 0; l < T; l++)
	{
		for(int i = 0; i < 2*N[l] - 1; i++)
		{
			for(int j = 0; j < N[l]; j++)
			{
				if(ls[l][i][j] >= 0){
					curr = ls[l][i][j];
					I = i;
					J = j;
					if(!search(ls, curr, i, j, l))
					{
						nu.push_back(ls[l][i][j]);
						ls[l][i][j]=-1;
					}
						
				}
				
			}
		}
		
		cout<<"Case #"<<l+1<<": ";
		sort(nu.begin(), nu.end());
		for(int i = 0; i < nu.size(); i++)
			cout<<nu[i]<<" ";
		cout<<endl;
		nu.erase(nu.begin(), nu.end());
	}
	
	
	return 0;
}
