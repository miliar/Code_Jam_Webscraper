// TicTac.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>


#include <string>

using namespace std;
int main(void)
{
	ifstream ifs;
	ofstream ofs;

	int T = 0;

	ifs.open("A-small-attempt1.in");
	ofs.open("result.txt");
	ifs >> T;
	if (T<1)
	{
		return -1;
	}
	
	for (int num=1; num<=T; ++num)
	{	
		char matrix[4][4];
		char *str = new char[4];
		bool decided=false;
		for (int i=0; i<4; ++i)
		{
			ifs >> str;
			for (int j=0; j<4; ++j)
			{
				matrix[i][j] = str[j];
			}
		}
		int count = 0;
		for (int i=0; i<4; ++i)
		{
			for (int j=0; j<4; ++j)
			{
				if (matrix[i][j] == 'T'||matrix[i][j] == 'X')
				{
					count++;
				} else break;
			}
			if (count == 4)
			{
				ofs<<"Case #"<<num<<": "<<"X won"<<endl;
				decided = true;
				break;
			} else count = 0;
			
			for (int j=0; j<4; ++j)
			{
				if (matrix[i][j] == 'O'||matrix[i][j] == 'T')
				{
					count++;
				} else break;
			}
			if (count == 4)
			{
				ofs<<"Case #"<<num<<": "<<"O won"<<endl;
				decided = true;
				break;
			} else count = 0;
		} 				
		if (decided)
		{
			continue;
		}
		//
		for (int i=0; i<4; ++i)
		{
			for (int j=0; j<4; ++j)
			{
				if (matrix[j][i] == 'T'||matrix[j][i] == 'X')
				{
					count++;
				} else break;
			}
			if (count == 4)
			{
				ofs<<"Case #"<<num<<": "<<"X won"<<endl;
				decided = true;
				break;
			} else count = 0;

			for (int j=0; j<4; ++j)
			{
				if (matrix[j][i] == 'O'||matrix[j][i] == 'T')
				{
					count++;
				} else break;
			}
			if (count == 4)
			{
				ofs<<"Case #"<<num<<": "<<"O won"<<endl;
				decided = true;
				break;
			} else count = 0;
		} 				
	
		if (decided)
		{
			continue;
		}
		//
		for (int i=0; i<4; ++i)
		{
			if (matrix[i][i] == 'O'|| matrix[i][i]=='T')
			{
				count++;	
			} else break;
		}
		if (count == 4)
		{
			ofs<<"Case #"<<num<<": "<<"O won"<<endl;
			decided = true;
			break;
		} else count = 0;

		if (decided)
		{
			continue;
		}

		for (int i=0; i<4; ++i)
		{
			if (matrix[i][i] == 'X'|| matrix[i][i]=='T')
			{
				count++;	
			} else break;
		}
		if (count == 4)
		{
			ofs<<"Case #"<<num<<": "<<"X won"<<endl;
			decided = true;
		} else count = 0; 

		if (decided)
		{
			continue;
		}	

		//
		for (int i=0; i<4; ++i)
		{
			if (matrix[i][3-i] == 'O'|| matrix[i][3-i]=='T')
			{
				count++;	
			} else break;
		}
		if (count == 4)
		{
			ofs<<"Case #"<<num<<": "<<"O won"<<endl;
			decided = true;
		} else count = 0;

		if (decided)
		{
			continue;
		}

		for (int i=0; i<4; ++i)
		{
			if (matrix[i][3-i] == 'X'|| matrix[i][3-i]=='T')
			{
				count++;	
			} else break;
		}
		if (count == 4)
		{
			ofs<<"Case #"<<num<<": "<<"X won"<<endl;
			decided = true;
		} else count = 0;

		if (decided)
		{
			continue;
		}

		for (int i=0; i<4; ++i)
		{
			for (int j=0; j<4;++j)
			{
				if (matrix[i][j] == '.')
				{
					ofs<<"Case #"<<num<<": "<<"Game has not completed"<<endl;
					decided = true;
					break;
				}
			}
			if (decided)
			{
				break;
			}
		}
		if (decided)
		{
			continue;
		}
		ofs<<"Case #"<<num<<": "<<"Draw"<<endl;
	}
	system("pause");
	return 0;
}





