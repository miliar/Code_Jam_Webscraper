#include <bits/stdc++.h>

using namespace std;

int M[4][4];

void update(int* F)
{
	int r;
	cin>>r;
	
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			cin>>M[i][j];
	
	for(int j=0; j<4; j++)
		F[M[r-1][j]-1]++;
}

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int F[16] = {};
		
		update(F);
		update(F);
		
		int ans = -1, cnt = 0;
		for(int i=1; i<=16; i++)
		{
			if(F[i-1] == 2)
			{
				ans = i;
				cnt++;
			}
		}
		
		cout<<"Case #"<<caso<<": ";
		
		if(cnt==0) cout<<"Volunteer cheated!"<<endl;
		else if(cnt==1) cout<<ans<<endl;
		else cout<<"Bad magician!"<<endl;
	}
	
	return 0;
}
