// basic file operations
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int Xwin[10];
int Owin[10];
int dotcnt;

int set_fr_cnt(int loc, char c)
{
	if(c == 'O')
	{
		if(++Owin[loc] == 4)
			return 1;
	}
	else if(c == 'X')
	{
		if(++Xwin[loc] == 4)
			return 2;
	}
	else if(c == 'T')
	{
		if(++Owin[loc] == 4)
			return 1;
		if(++Xwin[loc] == 4)
			return 2;
	}
	else
	{
		dotcnt++;
	}
	return 0;
}
void print_res(int res, int cnt)
{
		if(res == 1)
		{
			cout << "Case #"<< cnt <<": O won" << endl;
			return;
		}
		else if(res ==2)
		{
			cout << "Case #"<< cnt <<": X won" << endl;
			return;
		}
}
void printOut(string inp, int cnt)
{
	for(int i=0; i<10; i++)
	{
		Xwin[i] = 0;
		Owin[i] = 0;
	}
	dotcnt = 0;

	for(int i =0; i<16; i++)
	{
		int res = set_fr_cnt((i/4), inp[i]);
		if(res )
		{
			print_res(res,cnt);
			return;
		}
		res = set_fr_cnt((i%4) + 4, inp[i]);
		if(res )
		{
			print_res(res,cnt);
			return;
		}
	}
	for (int i=0; i<16; i+=5)
	{
		int res = set_fr_cnt(8,inp[i]);
		if(res )
		{
			print_res(res,cnt);
			return;
		}
	}
	for (int i=3; i<13; i+=3)
	{
		int res = set_fr_cnt(9,inp[i]);
		if(res )
		{
			print_res(res,cnt);
			return;
		}
	}
	if(dotcnt > 0)
	{
		cout << "Case #" << cnt << ": Game has not completed" << endl;
	}
	else
	{
		cout << "Case #" << cnt << ": Draw" << endl;
	}
	return;
}
int main () {
	ifstream myfile;
	myfile.open ("input");
	int cnt = 0;
	if ( myfile.is_open())
	{
		string line1;
		string line2;
		string line3;
		string line4;
		cnt++;
		getline (myfile, line1);
		cout << line1 << endl;
		while(myfile.good())
		{
			//process first 4
			getline(myfile, line1);
			getline(myfile, line2);
			getline(myfile, line3);
			getline(myfile, line4);
			printOut(line1+line2+line3+line4, cnt);
			//process first 4
			getline(myfile, line1);
			cnt++;
		}	

		myfile.close();
		return 0;
	}
}
