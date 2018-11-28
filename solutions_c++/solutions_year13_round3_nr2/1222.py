#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#define MAX_LENGTH 9999
using namespace std;

int main()
{
	FILE *in_file, *out_file;
	char in_string [MAX_LENGTH];
	char out_string[MAX_LENGTH];

	in_file  = fopen("in.txt",  "r");
	out_file = fopen("out.txt", "w");
	if ( in_file  == NULL ) { cout << "in.txt open error" <<  endl; exit(0); }
	if ( out_file == NULL ) { cout << "out.txt open error" << endl; exit(0); }

	int T = 0;
	fscanf(in_file, "%d\n", &T); //%I64d 
	cout << "T:" << T << endl;
	
	__int64 x, y;
	for ( int tloop=0; tloop<T; tloop++ )
	{
		fscanf(in_file, "%I64d %I64d\n", &x, &y);
		cout << "T:" << tloop+1 << " : " << x << " " << y << endl;

		string ans = "";
		__int64 tmp_x = 0, tmp_y = 0, loop = 0;
		while ( tmp_x != x || tmp_y != y )
		{
			if ( loop > 1000 ) break;
			loop++;
			char direction = ' ';
			bool is_x = true;
			if (tmp_x == x) is_x = false;
			if ( is_x )
			{
				int xlength = x - tmp_x;
				     if ( abs(xlength) >= loop ) xlength>0 ? direction='E' : direction='W';
				else if ( abs(xlength) <  loop ) xlength>0 ? direction='W' : direction='E';
			}
			else
			{
				int ylength = y - tmp_y;
				     if ( abs(ylength) >= loop ) ylength>0 ? direction='N' : direction='S';
				else if ( abs(ylength) <  loop ) ylength>0 ? direction='S' : direction='N';
			}
			switch ( direction )
			{
				case 'E' : tmp_x += loop; break;
				case 'W' : tmp_x -= loop; break;
				case 'N' : tmp_y += loop; break;
				case 'S' : tmp_y -= loop; break;
			}
			//cout << direction << " " << tmp_x << " " << tmp_y << endl;
			ans += direction;
		}

		sprintf(out_string, "Case #%d: %s\n", tloop+1, ans.c_str());
		fputs(out_string, out_file);
	}
	fclose (in_file);
	fclose (out_file);
}