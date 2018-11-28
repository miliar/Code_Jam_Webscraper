#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream f;
	ofstream of;
	f.open("a.in");
	of.open("a.outt");
	int t;
	f >> t;
	char tt[4][4];
	char h,v,o1,o2;
	int to=t;
	bool draw;
	bool win;
	while(t--)
	{
		draw=1;
		win=0;
		for(int j=0; j<4; ++j)
		for(int i=0; i<4; ++i)
		{
			f >> tt[i][j];
			if(tt[i][j] == 'T') tt[i][j]=255;
			if(tt[i][j] == '.') draw=0; 
		}
		
		for(int i=0; i<4;++i)
		{
			v =  tt[i][0] & tt[i][1] & tt[i][2] & tt[i][3];
			h =  tt[0][i] & tt[1][i] & tt[2][i] & tt[3][i];
			if(!win && (v == 'O' || v == 'X')){win=1;
				of << "Case #"<< to-t<< ": "<< v << " won"<< endl;}
			else if(!win && (h == 'O' || h == 'X')){win=1;
				of << "Case #"<< to-t<< ": "<<h << " won" << endl;}

			
		}
		o1 =  tt[0][0] & tt[1][1] & tt[2][2] & tt[3][3];
		o2 =  tt[3][0] & tt[2][1] & tt[1][2] & tt[0][3];
		if (!win && (o1 == 'O' || o1 == 'X')){win=1;
				of << "Case #"<< to-t<< ": "<<o1 << " won"<< endl;}
		else if (!win && (o2 == 'O' || o2 == 'X')){win=1;
				of << "Case #"<< to-t<< ": "<<o2 << " won"<< endl;}


		/*for(int j=0; j<4; ++j)
		{
		for(int i=0; i<4; ++i)
		{
			cout << tt[i][j];
		}
		cout << endl;
		}
		cout << endl;*/
		if(!draw && !win)
			of << "Case #"<< to-t<< ": "<< "Game has not completed"<< endl;
		else if (draw && !win)
			of << "Case #"<< to-t<< ": "<< "Draw"<< endl;
			
	}
	f.close();
	of.close();
	return 0;
}
