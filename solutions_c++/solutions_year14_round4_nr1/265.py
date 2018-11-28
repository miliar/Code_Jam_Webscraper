#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int discos[10010];
int used[10010];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++)
	{
		int N, X;
		cin >> N >> X;
		
		for(int i=0; i<N; i++)
			cin >> discos[i];
		
		sort(discos, discos+N);
		memset(used,0,sizeof(used));
		
		int ans=0;
		for(int i=N-1; i>=0; i--)
		{
			if(!used[i])
			{
				used[i]=1;
				ans++;
				
				int j=i-1;
				while(j>=0 && (used[j] || discos[j]+discos[i]>X))
					j--;
				
				if(j>=0) used[j]=1;
			}
		}
		
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
