#include <bits/stdc++.h>
using namespace std;

void test()
{
	int R, C;
	cin >> R >> C;
	vector<string> lines(R);
	for(size_t i =0; i<R; ++i)
		cin >> lines[i];
		
	int sol=0;
		
	
	for(size_t r =0; r<R; ++r)
		for(size_t c =0; c<C; ++c)
		{
			if (lines[r][c]=='.')
				continue;
				
			bool left = false, right = false, up=false, down=false;
				
			for(size_t c2=0;c2<c;++c2)
				if (lines[r][c2]!='.')
				{
					left = true;
					break;
				}
				
			for(size_t c2=c+1;c2<C;++c2)
				if (lines[r][c2]!='.')
				{
					right = true;
					break;
				}
				
			for(size_t r2=0;r2<r;++r2)
				if (lines[r2][c]!='.')
				{
					up = true;
					break;
				}
				
			for(size_t r2=r+1;r2<R;++r2)
				if (lines[r2][c]!='.')
				{
					down = true;
					break;
				}
				
			if ( (lines[r][c]=='<' && left)
			   ||(lines[r][c]=='>' && right)
			   ||(lines[r][c]=='^' && up)
			   ||(lines[r][c]=='v' && down))
			   continue;
			   
			if (left || right || up || down)
				sol++;
			else
			{
				cout << "IMPOSSIBLE";
				return;
			}
		}
		
	cout << sol;
}

int main()
{
	size_t c;
	cin >> c;
	for (size_t i = 1; i<=c; ++i)
	{
		cout << "Case #" << i << ": ";
		test();
		cout << endl;
	}
}
