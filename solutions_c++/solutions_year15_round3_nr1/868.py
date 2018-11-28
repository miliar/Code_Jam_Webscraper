#include <bits/stdc++.h>

using namespace std;

int R, C, W;
int memo1[1<<20];
int memo2[1<<20];

int g(int mask)
{
	if(memo2[mask] != -1) return memo2[mask];
	
	int opt = 0, i=0;
	while(i < C)
	{
		if((mask & (1<<i)) == 0)
		{
			int j = i;
			while(j < C && (mask & (1<<j)) == 0) j++;
			if(j - i >= W) opt += j - i - W + 1;
			
			i = j + 1;
		}
		else i++;
	}
	
	return memo2[mask] = opt;
}

int f(int mask)
{
	if(memo1[mask] != -1) return memo1[mask];
	
	int opt = g(mask);
	
	if(opt == 1) return memo1[mask] = 0;
	else
	{
		int x = 1<<30;
		for(int i=0; i<C; i++)
		{
			if((mask & (1<<i)) == 0)
			{
				int nmask = mask ^ (1<<i);
				if(g(nmask) >= 1) x = min(x, 1 + f(nmask));
			}
		}
		return memo1[mask] = x;
	}
}

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>R>>C>>W;
		memset(memo1, -1, sizeof(memo1));
		memset(memo2, -1, sizeof(memo2));
		int x = f(0);
		cout<<"Case #"<<caso<<": "<<(R-1) * (x + 1) + x + W <<endl;
	}
	
	return 0;
}
