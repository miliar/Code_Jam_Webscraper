#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define ll long long
#define ld long double
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define y0 isdnfviu
#define y1 asinhiv
#define fst first
#define snd second
#define count sdifnsugh

bool used[111];
int t,x,y;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for(int k=1; k<=t; k++)
	{
		memset(used,0,sizeof(used));
		cin >> x;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
			{
				cin >> y;
				if (i==x-1) used[y]=true;
			}
		cin >> x;
		int kol=0,ans=0;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
			{
				cin >> y;
				if (i==x-1 && used[y]) 
				{
					ans=y;
					kol++;
				} 
			}
		cout << "Case #" << k << ": ";	
		if (kol==0)	cout << "Volunteer cheated!\n";
		else if (kol>1) cout << "Bad magician!\n";
		else cout << ans << "\n";
	}
//	cin >> t;
	return 0;
}
