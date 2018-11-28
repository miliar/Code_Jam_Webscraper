#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
	int T, flag = 0;
	char xo[4][4];
	string ss;
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("out.txt");
	infile>>T;
	for(int i = 0; i < T; ++i)
	{
		flag = 0;
		//if(i != 0)
		//	infile>>ss;
		for(int t = 0; t < 4; ++t)
		{
			for(int k = 0; k < 4; ++k)
			{
				infile>>xo[t][k];
			}
		}
		//the row?
		for(int t = 0; t < 4; ++t)
		{
			int m = 0;
			if(xo[t][m] == 'T' || xo[t][m] == 'X')
			{
				m++;
				while(xo[t][m] == 'X' || xo[t][m] == 'T' && m < 4)
					m++;
				if(m >= 4)
				{
					flag = 1;
					stringstream ss;
					ss<<"Case #"<<i + 1<<": "<<"X won"<<endl;
					outfile<<ss.str().c_str();
					break;
				}
			}
			m = 0;
			if(xo[t][m] == 'T' || xo[t][m] == 'O')
			{
				m++;
				while(xo[t][m] == 'O' || xo[t][m] == 'T' && m < 4)
					m++;
				if(m >= 4)
				{
					flag = 1;
					stringstream ss;
					ss<<"Case #"<<i + 1<<": "<<"O won"<<endl;
					outfile<<ss.str().c_str();
					break;
				}
			}
		}
		if(flag)
			continue;
		//the column?
		for(int k = 0; k < 4; ++k)
		{
			int m = 0;
			if(xo[m][k] == 'T' || xo[m][k] == 'X')
			{
				m++;
				while(xo[m][k] == 'X' || xo[m][k] == 'T' && m < 4)
					m++;
				if(m >= 4)
				{
					flag = 1;
					stringstream ss;
					ss<<"Case #"<<i + 1<<": "<<"X won"<<endl;
					outfile<<ss.str().c_str();
					break;
				}
			}
			m = 0;
			if(xo[m][k] == 'T' || xo[m][k] == 'O')
			{
				m++;
				while(xo[m][k] == 'O' || xo[m][k] == 'T' && m < 4)
					m++;
				if(m >= 4)
				{
					flag = 1;
					stringstream ss;
					ss<<"Case #"<<i + 1<<": "<<"O won"<<endl;
					outfile<<ss.str().c_str();
					break;
				}
			}
		}
		if(flag)
			continue;
		//the diagonal?
		int t1 = 0, k1 = 0;
		if(xo[t1][k1] == 'T' || xo[t1][k1] == 'X')
		{
			t1++;
			k1++;
			while(xo[t1][k1] == 'X' || xo[t1][k1] == 'T' && t1 < 4 && k1 < 4)
			{
				t1++;
				k1++;
			}
			if(t1 >= 4 && k1 >= 4)
			{
				flag = 1;
				stringstream ss;
				ss<<"Case #"<<i + 1<<": "<<"X won"<<endl;
				outfile<<ss.str().c_str();
				continue;
			}
		}
		else if(xo[t1][k1] == 'T' || xo[t1][k1] == 'O')
		{
			t1++;
			k1++;
			while(xo[t1][k1] == 'O' || xo[t1][k1] == 'T' && t1 < 4 && k1 < 4)
			{
				t1++;
				k1++;
			}
			if(t1 >= 4 && k1 >= 4)
			{
				flag = 1;
				stringstream ss;
				ss<<"Case #"<<i + 1<<": "<<"O won"<<endl;
				outfile<<ss.str().c_str();
				continue;
			}
		}
		t1 = 0;
		k1 = 3;
		if(xo[t1][k1] == 'T' || xo[t1][k1] == 'X')
		{
			t1++;
			k1--;
			while(xo[t1][k1] == 'X' || xo[t1][k1] == 'T' && t1 < 4 && k1 >= 0)
			{
				t1++;
				k1--;
			}
			if(t1 >= 4 && k1 < 0)
			{
				flag = 1;
				stringstream ss;
				ss<<"Case #"<<i + 1<<": "<<"X won"<<endl;
				outfile<<ss.str().c_str();
				continue;
			}
		}
		else if(xo[t1][k1] == 'T' || xo[t1][k1] == 'O')
		{
			t1++;
			k1--;
			while(xo[t1][k1] == 'O' || xo[t1][k1] == 'T' && t1 < 4 && k1 >= 0)
			{
				t1++;
				k1--;
			}
			if(t1 >= 4 && k1 < 0)
			{
				flag = 1;
				stringstream ss;
				ss<<"Case #"<<i + 1<<": "<<"O won"<<endl;
				outfile<<ss.str().c_str();
				continue;
			}
		}
		//the draw?
		for(int t = 0; t < 4; ++t)
		{
			for(int k = 0; k < 4; ++k)
			{
				if(xo[t][k] == '.')
				{
					flag = 1;
					break;
				}
			}
			if(flag)
			{
				break;
			}
		}
		if(flag == 0)
		{
			stringstream ss;
			ss<<"Case #"<<i + 1<<": "<<"Draw"<<endl;
			outfile<<ss.str().c_str();
		}
		else if(flag == 1)
		{
			stringstream ss;
			ss<<"Case #"<<i + 1<<": "<<"Game has not completed"<<endl;
			outfile<<ss.str().c_str();
		}
	}
	infile.close();
	outfile.close();
	return 0;
}