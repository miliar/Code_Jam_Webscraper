#include <bits/stdc++.h>
using namespace std;

string f[3][14];
int win[3] = {1 , 2 , 0};
string ch[3] = {"P" , "R" , "S"};

int cnt[3];

int main()
{
	for(int k = 0 ; k < 3 ; k++)
		f[k][1] = min(ch[k] + ch[win[k]] , ch[win[k]] + ch[k]);
	for(int i = 1 ; i < 12 ; i++)
	{
		for(int k = 0 ; k < 3 ; k++)
		{
			f[k][i + 1] = min(f[k][i] + f[win[k]][i] , 
				f[win[k]][i] + f[k][i]);
		}
	}
	int test;scanf("%d" , &test);
	for(int t = 1 ; t <= test ; t++)
	{
		int n , p , r , s;
		scanf("%d%d%d%d" , &n , &r , &p , &s);
		
		string ans = "";
		for(int k = 0 ; k < 3 ; k++)
		{
			cnt[0] = cnt[1] = cnt[2] = 0;
			for(int i = 0 ; i < f[k][n].length(); i++)
			{
				if(f[k][n][i] == 'P')cnt[0]++;
				if(f[k][n][i] == 'R')cnt[1]++;
				if(f[k][n][i] == 'S')cnt[2]++;
			}
			if(cnt[0] == p && cnt[1] == r && cnt[2] == s)
				if(ans == "" || f[k][n] < ans)
					ans = f[k][n];
		}
		printf("Case #%d: " , t);
		if(ans == "")cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}