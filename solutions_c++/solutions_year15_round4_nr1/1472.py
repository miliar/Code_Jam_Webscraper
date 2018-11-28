#include <bits/stdc++.h>
using namespace std;
char arr[105][105]; int R, C;
bool check (int r, int c, char l)
{
	if (l=='^')
	{
		for (int z=r-1; z>=1; z--)
		{
			if (arr[z][c]!='.') return true; 
		}
		return false; 
	}
	else if (l=='v')
	{
		for (int z=r+1; z<=R; z++)
		{
			if (arr[z][c]!='.') return true; 
		}
		return false; 
	}
	else if (l=='>')
	{
		for (int z=c+1; z<=C; z++)
		{
			if (arr[r][z]!='.') return true;
		}
		return false;
	}
	else
	{
		for (int z=c-1; z>=1; z--)
		{
			if (arr[r][z]!='.') return true; 
		}
		return false; 
	}
}
int main()
{
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	int T; cin >> T;
	for (int g=0; g<T; g++)
	{
		memset(arr,0,sizeof(arr));
		cin >>R >> C; 
		for (int y=1; y<=R; y++)
		{
			for (int z=1; z<=C; z++) cin >> arr[y][z]; 
		}
		int flag=0, ans=0; 
		for (int y=1; y<=R; y++)
		{
			for (int z=1; z<=C; z++)
			{
				if (arr[y][z]=='.') continue; 
				if (check(y, z, arr[y][z])) continue;
				ans++; 
				if (check(y, z, '^')) continue;
				if (check(y,z,'>')) continue;
				if (check(y, z, '<')) continue;
				if (check(y, z, 'v')) continue; 
				flag=1; break; 
			}
			if (flag) break;
		}	
		cout << "Case #" << g+1 << ": "; 
		if (flag)
		{
			cout << "IMPOSSIBLE" << '\n'; 
		}
		else
		{
			cout << ans << '\n'; 
		}
	}
}
