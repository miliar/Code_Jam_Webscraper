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
#include <algorithm>
#include <random>
#include <iomanip>


using namespace std;



int main()
{

	/*ifstream fin("input.txt");
	ofstream fout("output.txt");*/

	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.out");

	int T;
	fin>>T;

	for (int cnt=1; cnt<=T; cnt++)
	{
		int R,C,W;
		fin>>R>>C>>W;
		if (R==1)
		{
			if (C%W==0)
			{
				fout<<"Case #"<<cnt<<": "<<C/W-1+W<<endl;
			}
			else
			{
				fout<<"Case #"<<cnt<<": "<<C/W+W<<endl;
			}
		}
		else
		{
			if (C%W==0)
			{
				fout<<"Case #"<<cnt<<": "<<R*C/W-1+W<<endl;
			}
			else
			{
				fout<<"Case #"<<cnt<<": "<<R*C/W-1+C/W+W<<endl;
			}
		}
	}

			

	


	system("pause");
}

