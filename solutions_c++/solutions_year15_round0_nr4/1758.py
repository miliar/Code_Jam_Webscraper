#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include<algorithm>
#include <random>
#include<iomanip>


using namespace std;




int main()
{

	/*ifstream fin("input.txt");
	ofstream fout("output.txt");*/

	ifstream fin("D-small-attempt1.in");
	ofstream fout("output.out");
	
	vector<int> Matrix[5][5];

	Matrix[1][1].push_back(-1);
	Matrix[1][2].push_back(2);
	Matrix[1][3].push_back(-1);
	Matrix[1][4].push_back(2);
	Matrix[2][1].push_back(2);
	Matrix[2][2].push_back(2);
	Matrix[2][3].push_back(2);
	Matrix[2][3].push_back(3);
	Matrix[2][4].push_back(2);
	Matrix[3][1].push_back(-1);
	Matrix[3][2].push_back(2);
	Matrix[3][2].push_back(3);
	Matrix[3][3].push_back(3);
	Matrix[3][4].push_back(2);
	Matrix[3][4].push_back(3);
	Matrix[3][4].push_back(4);
	Matrix[4][1].push_back(2);
	Matrix[4][2].push_back(2);
	Matrix[4][3].push_back(2);
	Matrix[4][3].push_back(3);
	Matrix[4][3].push_back(4);
	Matrix[4][4].push_back(2);
	//Matrix[4][4].push_back(3);
	Matrix[4][4].push_back(4);


	int T;
	fin>>T;

	for (int cnt=1; cnt<=T; cnt++)
	{
		int X,R,C;
		fin>>X>>R>>C;


		if (X==1)
			fout<<"Case #"<<cnt<<": GABRIEL"<<endl;
		else
		{
			vector<int>::iterator it=Matrix[R][C].begin();
			bool find=false;
			for (;it!=Matrix[R][C].end(); it++)
			{
				if (*it==X)
				{
					find=true;
					break;
				}
			}
			if (find==true)
				fout<<"Case #"<<cnt<<": GABRIEL"<<endl;
			else
				fout<<"Case #"<<cnt<<": RICHARD"<<endl;
		}
	}



	



	system("pause");
}

