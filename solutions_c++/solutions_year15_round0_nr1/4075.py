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

	ifstream fin("A-large.in");
	ofstream fout("output.out");

	

	int T;
	fin>>T;
	for (int i=1; i<=T; i++)
	{
		int S_max;
		fin>>S_max;
		char *Aud=new char [S_max+1];
		for (int j=0; j<=S_max; j++)
			fin>>Aud[j];

		/*for (int j=0; j<=S_max; j++)
			cout<<Aud[j];
		cout<<endl;*/
		//getchar();

		int cur_num=0;
	    int add_num=0;
		for (int j=0; j<=S_max; j++)
		{
			if (Aud[j]!='0')
			{
				if (cur_num>=j)
					cur_num=cur_num+Aud[j]-'0';
				else
				{
					add_num=add_num+j-cur_num;
					cur_num=j+Aud[j]-'0';
				}
				//cout<<"cur_num="<<cur_num<<" add_num="<<add_num<<endl;
			}
		}
		delete []Aud;
		
		fout<<"Case #"<<i<<": "<<add_num<<endl;
	}


	



	system("pause");
}

