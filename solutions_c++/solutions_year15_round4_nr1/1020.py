#include <bits/stdc++.h>
//#define DEBUG

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef pair<ll,ll> pll;
typedef vector<ll> vll;


int main()
{
	#ifndef DEBUG

    ifstream in("2a_l.in");
    cin.rdbuf(in.rdbuf());
    ofstream out("2a_l.out");
    cout.rdbuf(out.rdbuf());

    #endif
	 
	int T;
	cin>>T;
	for(int X = 1; X <= T; X++)
	{
		int R,C;
		cin>>R>>C;
		
		vector<string> grid(R);
		for(int i = 0; i < R; i++)
			cin>>grid[i];
		vector<int> up(C,-1), down(C,-1), left(R,-1), right(R,-1);
		for(int i = 0; i <  R;i++)
		{
			for(int j = 0; j < C; j++)
			{
				if(grid[i][j] != '.')
				{
					if(up[j] == -1 || i < up[j])
						up[j] = i;
					if(down[j] == -1 || i > down[j])
						down[j] = i;
					if(left[i] == -1 || j < left[i])
						left[i] = j;
					if(right[i] == -1 || j > right[i])
						right[i] = j;
				}
			}
		}
		int cnt = 0;
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				if(grid[i][j] != '.')
				{
					if(grid[i][j] == '>' && right[i] != j ||
					   grid[i][j] == '<' && left[i] != j ||
					   grid[i][j] == '^' && up[j] != i ||
					   grid[i][j] == 'v' && down[j] != i)
				   {
					  continue;
				   }
				   else
				   {
					   if(left[i] == j && right[i] == j && up[j] == i && down[j] == i)
					   {
						   cnt = -1;
						   break;
					   }
					   else cnt++;
				   }
						
						
				}
			}
			if(cnt == -1)	break;
		}
		cout<<"Case #"<<X<<": ";
		if(cnt == -1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<cnt<<endl;
	}
	
	return 0;
}