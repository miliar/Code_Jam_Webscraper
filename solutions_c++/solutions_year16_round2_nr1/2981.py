#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;

int checkSleep(int count[]);

int main(void)
{
	ifstream file;
	file.open("A-large.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for (int cc = 1; cc <= caseNo; cc++)
	{
		char ch[2001];
		file >> ch;
		int num[10];
		int z = 0, e = 0, r = 0, o = 0, n = 0, t = 0, w = 0, h = 0, f = 0, u = 0, i = 0, v = 0, s = 0, x = 0, g = 0;

		for (int tt = 0; ch[tt] != '\0'; tt++)
		{
			if (ch[tt] == 'Z')
				z++;
			else if (ch[tt] == 'E')
				e++;
			else if (ch[tt] == 'R')
				r++;
			else if (ch[tt] == 'O')
				o++;
			else if (ch[tt] == 'N')
				n++;
			else if (ch[tt] == 'T')
				t++;
			else if (ch[tt] == 'W')
				w++;
			else if (ch[tt] == 'H')
				h++;
			else if (ch[tt] == 'F')
				f++;
			else if (ch[tt] == 'U')
				u++;
			else if (ch[tt] == 'I')
				i++;
			else if (ch[tt] == 'V')
				v++;
			else if (ch[tt] == 'S')
				s++;
			else if (ch[tt] == 'X')
				x++;
			else if (ch[tt] == 'G')
				g++;
		}

		num[0] = z;
		e -= z;
		r -= z;
		o -= z;
		z = 0;
		num[8] = g;
		e -= g;
		i -= g;
		h -= g;
		t -= g;
		g = 0;
		num[3] = h;
		t -= h;
		r -= h;
		e = e - h * 2;
		h = 0;
		num[2] = w;
		t -= w;
		o -= w;
		w = 0;
		num[4] = r;
		f -= r;
		o -= r;
		u -= r;
		r = 0;
		num[1] = o;
		n -= o;
		e -= o;
		o = 0;
		num[6] = x;
		s -= x;
		i -= x;
		x = 0;
		num[7] = s;
		e = e - s * 2;
		v -= s;
		n -= s;
		s = 0;
		num[5] = v;
		f -= v;
		i -= v;
		e -= v;
		v = 0;
		num[9] = i;

		char result[700];
		int count = 0;
		for (int tt = 0; tt <= 9; tt++)
		{
			for (int ttt = 0; ttt < num[tt]; ttt++)
			{
				result[count] = tt + 48;
				count++;
			}
		}
		result[count] = '\0';



		


		output << "Case #" << cc << ": ";
		output << result << "\n";
	}
}