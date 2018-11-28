#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	int n;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		bool visited[11];
		for (int j = 0; j < 11; ++j)
			visited[j] = false;
		
		long long k = n;
		int s = 1;
		while(visited[10] == false)
		{

			while( k > 0)
			{
				visited[k%10] = true;
				k=k/10;
			}
			s++;
			k = s*n;
			visited[10] = true;
			for (int j=0; j<10; j++)
				visited[10] &= visited[j];
		}
		cout<<"Case #"<<i<<": "<<(s-1) * n<<endl;
	}
}