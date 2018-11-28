/*
 * A.CPP
 *
 *  Created on: 13-Apr-2013
 *      Author: sandip
 */

#include <iostream>
#include <vector>
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

	ifstream in("C:\\Users\\Sandip\\Downloads\\A-small-attempt0.in",ifstream::in);
	ofstream out("C:\\Users\\Sandip\\Downloads\\A-small-attempt0.out",ofstream::out);

	string strTestCase;
	getline(in,strTestCase);
	nTestCase = atol(strTestCase.c_str());

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
	int game1[4][4], game2[4][4];
	int first , second;

	in>>first;
	first--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			in >> game1[i][j];
		}
	}
	in>>second;
	second--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			in >> game2[i][j];
		}
	}
	
	int count=0;
	int card=-1;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(game1[first][i]==game2[second][j])
			{
				count++;
				card =  game1[first][i];
			}
		}
	}
	if(count==1)
		out<< card;
	else if(count > 1)
		out<< "Bad magician!";
	else
		out << "Volunteer cheated!";

}
