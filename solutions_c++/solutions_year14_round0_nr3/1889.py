#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

struct Coor
{
	Coor(int x1,int y1)
		:x(x1),y(y1)
	{}
	int x;
	int y;
};

vector<vector<char> > visAll;
int r,c,m;

bool ex( vector<bool>& bNeibor, int cur,const vector<Coor>& neibors, vector<vector<char> > vis, int sp );

bool isInside( int i, int j )
{
	return i >=0 && i < r && j >= 0 && j < c;
}

bool tryExpand( int oi, int oj, vector<vector<char> > vis,int sp )
{
	if(vis[oi][oj] == '+')
	{
		vis[oi][oj] = '.';
		sp--;
		if(sp==0)
		{
			visAll = vis;
			return true;
		}
	}


	int off[] = {0,1,-1};
	vector<Coor> neibors;
	for( int k = 0; k < 3; ++k )
	{
		for( int l = 0; l < 3; ++l )
		{
			if(k==0&&l==0)
				continue;
			int x = oi+off[k];
			int y = oj+off[l];
			if(isInside(x,y)&&vis[x][y]=='+')
				neibors.push_back(Coor(x,y));
		}
	}

	if(sp-(int)neibors.size()<0)
		return false;
	sp -= (int)neibors.size();

	for( int i = 0; i < neibors.size(); ++i )
	{
		vis[neibors[i].x][neibors[i].y] = '.';
	}
	if(sp==0)
	{
		visAll = vis;
		return true;
	}

	for( int i = 0; i < neibors.size(); ++i )
		if(tryExpand(neibors[i].x,neibors[i].y,vis,sp))
			return true;
	/*if(neibors.size()>0)
	{
	vector<bool> bNeibor(neibors.size(),false);
	return ex( bNeibor,0,neibors,vis, sp);
	}*/
	return false;
}

bool ex( vector<bool>& bNeibor, int cur,const vector<Coor>& neibors, vector<vector<char> > vis, int sp )
{
	if( cur == neibors.size()-1 )
	{
		for( int i = 0; i < bNeibor.size(); ++i )
		{
			if(bNeibor[i])
				if(tryExpand(neibors[i].x,neibors[i].y,vis,sp))
					return true;
		}
	}
	else
	{
		bNeibor[cur] = true;
		if(ex(bNeibor,cur+1,neibors,vis,sp))
			return true;
		bNeibor[cur] = false;
		if(ex(bNeibor,cur+1,neibors,vis,sp))
			return true;
	}

	return false;
}



int main()
{
	ifstream cin("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");
	int T;
	cin >> T;
	for( int s = 1; s <= T; ++s )
	{
		cin >>r>>c>>m;
		int sp = r*c-m;

		vector< vector<char> > a(r);

		for( int i = 0; i < r; ++i )
		{
			a[i].resize(c);
			for( int j = 0; j < c; ++j )
				a[i][j] = '+';
		}

		bool isPos = false;
		for( int i = 0; i < r; ++i )
		{
			for( int j = 0; j < c; ++j )
				if(tryExpand(i,j,a, sp))
				{
					visAll[i][j] = 'c';
					goto POSSIBLE;
					isPos = true;
				}
		}
		
		if( isPos )
		{
POSSIBLE:
			cout << "Case #" << s << ": "<<endl;
			for( int i = 0; i < r; ++i )
			{
				for( int j = 0; j < c; ++j )
				{
					cout << (visAll[i][j]=='+' ? '*':visAll[i][j]);
				}
				cout << endl;
			}
		}
		else
		{
			cout << "Case #" << s << ": "<<endl;
			cout << "Impossible" << endl;
		}
	}
	return 0;
}