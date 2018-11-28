#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int R, C;
char map[100][100];

bool bad(int r, int c, char dir)
{
	int x=0;
	int y=0;
	
	switch(dir)
	{
		case '^': y=-1; break;
		case '<': x=-1; break;
		case '>': x= 1; break;
		case 'v': y= 1; break;
	}
	
	c+=x;
	r+=y;
	while(r>=0 && c>=0 && r<R && c<C)
	{
		if (map[r][c] != '.') return false;
		c+=x;
		r+=y;
	}
	return true;
}

int main()
{ 
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int numCases;
	fin >> numCases;
	
	for (int caseNumber=1; caseNumber<=numCases; caseNumber++)
	{
		fout << "Case #" << caseNumber << ": ";
		
		fin >> R >> C;
		string lineChange;
		getline(fin, lineChange);
		
		for (int r=0; r<R; r++)
		{
			for (int c=0; c<C; c++)
				fin >> map[r][c];
			getline(fin, lineChange);
		}
		
		int count = 0;
		for (int r=0; r<R; r++)
		for (int c=0; c<C; c++)
		{
			if (map[r][c] != '.' && bad(r, c, map[r][c]))
			{
				if (bad(r, c, '^') && bad(r, c, '<') && bad(r, c, '>') && bad(r, c, 'v'))
					goto impossible;
				else
					count++;
			}
		}
		
		fout <<  count << endl;
		continue;
		
		impossible:
		fout << "IMPOSSIBLE" << endl;
	}
 
    return 0;
}