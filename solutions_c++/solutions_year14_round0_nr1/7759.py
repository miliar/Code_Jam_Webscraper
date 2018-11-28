// MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream ifs("A-small-attempt0.in");

	int n;

	ifs>>n;

	for(int i = 0; i < n;i++)
	{

		int m1,m2;
		vector<int> v1,v2;
		int index1, index2;
		vector<int> result;

		ifs>>m1;

		for(int j = 0;j<16;j++)
		{
			int temp;
			ifs>>temp;
			v1.push_back(temp);
		}


		index1 = (m1-1)*4;



		ifs>>m2;

		for(int j = 0;j<16;j++)
		{
			int temp;
			ifs>>temp;
			v2.push_back(temp);
		}


		index2 = (m2-1)*4;


		for(int j = index1;j<index1+4;j++)
		{
			for (int k = index2; k<index2+4;k++)
			{
				if (v1[j] == v2[k])
				{
					result.push_back(v1[j]);
				}
			}
		}

		if(result.size() == 1)
		{
			int temp = result[0];
			cout<<"Case #"<<(i+1)<<": "<<temp<<endl;
		}


		if(result.size() == 0)
		{

			cout<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;
		}

		if(result.size() > 1)
		{

			cout<<"Case #"<<(i+1)<<": Bad magician!"<<endl;
		}




	}


	return 0;
}

