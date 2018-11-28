#include <bits/stdc++.h>
using namespace std;

int r,c;
vector<vector<char> > m;

char first_hit(int x, int y, int dx, int dy)
{
	for(int i=x+dx, j=y+dy;i>=0 && i<r && j>=0 && j<c;i+=dx, j+=dy)
	{
		if(m[i][j] != '.') return m[i][j];
	}
	return 'b';
}

void test(int x,int y)
{
	char c=m[x][y];
	int dx,dy;
	if(c=='.') return;
	if(c=='<'){dx=0;dy=-1;}
	if(c=='>'){dx=0;dy=1;}
	if(c=='^'){dx=-1;dy=0;}
	if(c=='v'){dx=1;dy=0;}
	
	if(first_hit(x,y,dx,dy)=='b') m[x][y]='?';
}

int main()
{
	int t;
	cin >> t;
	for(int ta=1;ta<=t;++ta)
	{
		cout << "Case #" << ta << ": ";
		cin >> r >> c;
		m.assign(r,vector<char>(c));
		for(int i=0;i<r;++i) for(int j=0;j<c;++j)
			cin >> m[i][j];
		for(int i=0;i<r;++i) for(int j=0;j<c;++j)
			test(i,j);
		bool possible=true;
		for(int i=0;i<r;++i) for(int j=0;j<c;++j) if(m[i][j] == '?')
		{
			if(first_hit(i,j,0,-1)=='b' && first_hit(i,j,0,1)=='b' && first_hit(i,j,-1,0)=='b' && first_hit(i,j,1,0)=='b')
				possible = false;
		}
		int resp=0;
		for(int i=0;i<r;++i) for(int j=0;j<c;++j) if(m[i][j] == '?')
			resp++;
		
		if(possible) cout << resp << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}
