#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

bool chk( int mapX, int mapY, int map[101][101] )
{
	for( int i = 0; i < mapX; i++ )
	{		
		for( int j = 0; j < mapY; j++ )
		{
			bool row = true;
			bool col = true;
			for( int rr = 0; rr < mapX; rr++ )
				row *= map[i][j] >= map[rr][j] ? true : false;
			for( int cc = 0; cc < mapY; cc++ )
				col *= map[i][j] >= map[i][cc] ? true : false;
			if( !row && !col )
			{
				return false;
			}
		}
	}
	return true;
}

int main()
{
	int T = 0;
	int map[101][101] = { 0 };
	int mapX, mapY;
	
	ifstream inf;
	ofstream oufile;
	inf.open("B-large.in");
	oufile.open("out.txt");
	string oup;

	inf >> T;
	for( int  c = 0; c < T; c++ )
	{
		inf >> mapX >> mapY;
		for( int i = 0; i < mapX; i++ )
		{		
			for( int j = 0; j < mapY; j++ )
			{
				inf >> map[i][j];
			}
		}
		if (chk(mapX, mapY, map))
		{
			stringstream out;
			out << c + 1;
			oup = "Case #" + out.str() + ": YES\n"; 
			oufile << oup;
		}
		else
		{
			stringstream out;
			out << c + 1;
			oup = "Case #" + out.str() + ": NO\n"; 
			oufile << oup;
		}
	}
	inf.close();
	oufile.close();

	system("pause");
	return 0;
}