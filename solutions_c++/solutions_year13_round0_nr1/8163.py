/*
 * A.CPP
 *
 *  Created on: 13-Apr-2013
 *      Author: sandip
 */

#include <iostream>
#include <vector>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <string>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <iomanip>


using namespace std;
void solution(ifstream &in ,ofstream &out);

int main()
{
	long long nTestCase = 0;

	ifstream in("/home/sandip/Downloads/A-small-attempt0.in",ifstream::in);
	ofstream out("/home/sandip/Downloads/A-small-attempt0.out",ofstream::out);

	string strTestCase;
	getline(in,strTestCase);
	nTestCase = atoll(strTestCase.c_str());

	for(int i=0; i< nTestCase; i++)
	{
		out<<"Case #"<<i+1<<": ";
		solution(in, out);
		out<<endl;
	}

	in.close();
	out.close();
	return 0;
}

void solution(ifstream &in, ofstream &out)
{
	char game[4][5];
	for(int i=0;i<4;i++)
	{
		in>>game[i];
	}

	int nX=0,nO=0;
	int nT=0;
	if(game[0][0]=='X') nX++;
	if(game[1][1]=='X') nX++;
	if(game[2][2]=='X') nX++;
	if(game[3][3]=='X') nX++;

	if(game[0][0]=='O') nO++;
	if(game[1][1]=='O') nO++;
	if(game[2][2]=='O') nO++;
	if(game[3][3]=='O') nO++;

	if(game[0][0]=='T') nT++;
	if(game[1][1]=='T') nT++;
	if(game[2][2]=='T') nT++;
	if(game[3][3]=='T') nT++;

	if(nX>3)
		{
			out<<"X won";
			return;
		}
	if(nO>3)
		{
			out<<"O won";
			return;
		}

	if(nX==3&&nT==1)
		{
			out<<"X won";
			return;
		}
	if(nO==3&&nT==1)
		{
			out<<"O won";
			return;
		}

	nX=0,nO=0;
	nT=0;
	if(game[0][3]=='X') nX++;
	if(game[1][2]=='X') nX++;
	if(game[2][1]=='X') nX++;
	if(game[3][0]=='X') nX++;

	if(game[0][3]=='O') nO++;
	if(game[1][2]=='O') nO++;
	if(game[2][1]=='O') nO++;
	if(game[3][0]=='O') nO++;

	if(game[0][3]=='T') nT++;
	if(game[1][2]=='T') nT++;
	if(game[2][1]=='T') nT++;
	if(game[3][0]=='T') nT++;

	if(nX>3)
			{
				out<<"X won";
				return;
			}
		if(nO>3)
			{
				out<<"O won";
				return;
			}

		if(nX==3&&nT==1)
			{
				out<<"X won";
				return;
			}
		if(nO==3&&nT==1)
			{
				out<<"O won";
				return;
			}
	int nDot=0;
	for(int i=0;i<4;i++)
	{
		nX=0,nO=0;
		nT=0;
		for(int j=0;j<4;j++)
		{
			if(game[i][j]=='X') nX++;
			if(game[i][j]=='O') nO++;
			if(game[i][j]=='T') nT++;
			if(game[i][j]=='.') nDot++;
		}
		if(nX>3)
			{
				out<<"X won";
				return;
			}
		if(nO>3)
			{
				out<<"O won";
				return;
			}

		if(nX==3&&nT==1)
			{
				out<<"X won";
				return;
			}
		if(nO==3&&nT==1)
			{
				out<<"O won";
				return;
			}
	}
	for(int i=0;i<4;i++)
	{
		nX=0,nO=0;
		nT=0;
		for(int j=0;j<4;j++)
		{
			if(game[j][i]=='X') nX++;
			if(game[j][i]=='O') nO++;
			if(game[j][i]=='T') nT++;
			if(game[j][i]=='.') nDot++;
		}
		if(nX>3)
			{
				out<<"X won";
				return;
			}
		if(nO>3)
			{
				out<<"O won";
				return;
			}

		if(nX==3&&nT==1)
			{
				out<<"X won";
				return;
			}
		if(nO==3&&nT==1)
			{
				out<<"O won";
				return;
			}
	}
	if(nDot>1)
		out << "Game has not completed";
	else
		out << "Draw";

}




