// lawnweed.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>

#include <string>

using namespace std;
int main(void)
{
	ifstream ifs;
	ofstream ofs;

	int T = 0;
	int M = 0;
	int N = 0;

	ifs.open("B-small-attempt2.in");
	ofs.open("result.txt");
	ifs >> T;
	if (T<1)
	{
		return -1;
	}
	for (int num=1; num<=T; ++num)
	{
		ifs >> N >> M;
		//ofs<<N<<" "<<M<<endl;
		vector< vector<int> > matrix;
		
		for (int i=0; i<N; ++i)
		{
			vector<int> vec;
			int value;
			for(int j = 0; j < M;++j){
				ifs >> value;
				vec.push_back(value);
			}
			matrix.push_back(vec);
		}

		vector<int> pos;
		for (int i=0; i<N; ++i)
		{
			for (int j=0; j<M-1; ++j)
			{ 
				if (matrix.at(i).at(j) != matrix.at(i).at(j+1))
				{
					pos.push_back(i);
					break;
				}	
			}
		}
		
		bool allequal = true;
		bool work = true;
		if (pos.size()!=0)
		{	
			for (int i=0; i<M; ++i)
			{
				for (int j=0; j < pos.size()-1; ++j)
				{ 
					if (matrix.at(pos.at(j)).at(i) != matrix.at(pos.at(j+1)).at(i))
					{
						allequal = false;
						break;
					}
				}
				if(!allequal) {
					work = false;
					break;
				}
				for (int k=0; k < N;++k)
				{
					if (matrix.at(pos.at(0)).at(i) < matrix.at(k).at(i))
					{
						work = false;
					}	
				}
			}
		}
		
		if (work)
		{
			ofs<<"Case #"<<num<<": "<<"YES"<<endl;
		}else{
			ofs<<"Case #"<<num<<": "<<"NO"<<endl;
		}
	}
	system("pause");
	return 0;
}



