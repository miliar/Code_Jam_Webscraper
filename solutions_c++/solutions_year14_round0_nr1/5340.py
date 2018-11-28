#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

void solve()
{
	int A1, A2, C, C1, C2;
	int X1[4][4], X2[4][4];
	cin>>A1;
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	cin>>X1[i][j];
	cin>>A2;
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	cin>>X2[i][j];
	
	bool flag = false, bad = false;
	for(int i = 0; i < 4; i++)
	{
		int C1 = X1[A1-1][i];
		for(int j = 0; j < 4; j++)
		{
			int C2 = X2[A2-1][j];
			if(C1 == C2 && flag)
			bad = true;
			else if(C1 == C2)
			{
				flag = true;
				C = C1;
			}
		}
	}
	
	if(bad)
	cout<<"Bad magician!\n";
	else if(flag)
	cout<<C<<endl;
	else
	cout<<"Volunteer cheated!\n";
}

int main(void)
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, t = 1;
	cin>>T;
	while(T--)
	{
		cout<<"Case #"<<t++<<": ";
		solve();
	}
	return 0;
}
