#include<iostream>
#include<fstream>
using namespace std;
const int M = 4;
const int MAX = 17;


int main()
{
	int ncase;
	cin >> ncase;
	int num = 1;
	while(num <= ncase)
	{
		

		int first[M][M] = {0};
		int second[M][M] = {0};
		bool judge[MAX] = {false};

		int firstA = 0;
		int secondA = 0;
		cin >> firstA;
		for(int i = 0; i < M; ++i)
		{
			for(int j = 0; j < M; ++j)
			{
				cin >>first[i][j];
				if(i + 1 == firstA)
				{
					judge[first[i][j]] = true;
				}
			}
		}

		cin >> secondA;
		int match = 0;
		int out = 0;
		for(int i = 0; i < M; ++i)
		{
			for(int j = 0; j < M; ++j)
			{
				cin>>second[i][j];
				if(i + 1 == secondA)
				{
					if(judge[second[i][j]])
					{
						++match;
						out = second[i][j];
					}
				}
			}
		}
		ofstream fout("out.txt", std::ios_base::app );
		if(match<= 0)
		{
			fout<< "Case #"<<num<<": Volunteer cheated!"<<endl;
		}
		else if (match == 1)
		{
			fout<< "Case #"<<num<<": "<<out<<endl;
		}
		else if (match > 1)
		{
			fout<< "Case #"<<num<<": Bad magician!"<<endl;
		}
		fout.flush();
		fout.close();
		++num;
	}
	return 0;
}