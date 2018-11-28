#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;
int main()
{
	char mult[8][8] = {
		{ '1', 'i', 'j', 'k', '2', 'I', 'J', 'K' },
		{ 'i', '2', 'k', 'J', 'I', '1', 'K', 'j' },
		{ 'j', 'K', '2', 'i', 'J', 'k', '1', 'I' },
		{ 'k', 'j', 'I', '2', 'K', 'J', 'i', '1' },
		{ '2', 'I', 'J', 'K', '1', 'i', 'j', 'k' },
		{ 'I', '1', 'K', 'j', 'i', '2', 'k', 'J' },
		{ 'J', 'k', '1', 'I', 'j', 'K', '2', 'i' },
		{ 'K', 'J', 'i', '1', 'k', 'j', 'I', '2' },
	};
	map <char, int> res;
	res['1'] = 0;
	res['i'] = 1;
	res['j'] = 2;
	res['k'] = 3;
	res['2'] = 4;
	res['I'] = 5;
	res['J'] = 6;
	res['K'] = 7;
	std::ifstream infile("C-small-attempt0.in");

	ofstream myfile("Dijkstra.out");
	int tests;
	infile >> tests;
	for (int m = 1; m < tests+1; m++)
	{
		int testLen, repeat;
		infile >> testLen >> repeat;
		string input1;
		infile >> input1;
		string input = input1;
		for (int i = 0; i < repeat - 1; i++)
		{
			input += input1;
		}
		vector <int> Icount;
		if (input[0] == 'i')
			Icount.push_back(1);
		char iAcc = input[0];
		int t = 0, t1 = 0;
		for (int i = 0; i < input.length() - 2; i ++)
		{
			if (Icount.size() > 0)
				break;
			t = res.find(iAcc)->second;
			t1 = res.find(input[i + 1])->second;
			iAcc = mult[t][t1];
			if (iAcc == 'i')
			{
				Icount.push_back((i + 2));
			}
		}
		if (Icount.size() != 0)
		{
			vector <int> jcount;
			for (int i = 0; i < Icount.size(); i++)
			{
				if (input[Icount[i]] == 'j')
					jcount.push_back(Icount[i]+1);
				char jAcc = input[(Icount[i])];
				t = 0, t1 = 0;
				for (int j = (Icount[i]); j < input.length() - 1; j ++)
				{
					if (jcount.size() > 0)
						break;
					t = res.find(jAcc)->second;
					t1 = res.find(input[j + 1])->second;
					jAcc = mult[t][t1];
					if (jAcc == 'j')
						jcount.push_back((j + 2));
				}
			}
			bool flag = true;
			if (jcount.size() != 0)
			{
				for (int i = 0; i < jcount.size(); i++)
				{
					if (input[jcount[i]] == 'k' && jcount[i]== input.length()-1)
					{
						myfile << "Case #" << m << ": " << "YES" << endl;
						flag = false;
						break;
					}
					char jAcc = input[(jcount[i])];
					t = 0, t1 = 0;
					int j;
					for (j = (jcount[i]); j < input.length()-1; j++)
					{
						t = res.find(jAcc)->second;
						t1 = res.find(input[j + 1])->second;
						jAcc = mult[t][t1];
					}
					if (jAcc == 'k' && ((j--) == (input.length() - 1))){
						myfile << "Case #" << m << ": " << "YES" << endl;
						flag = false;
						break;
					}
				}
				if (flag)
				{
					myfile << "Case #" << m << ": " << "NO" << endl;
				}
			}
			else
			{
				myfile << "Case #" << m << ": " << "NO" << endl;
			}
		}
		else 
		{
			myfile << "Case #" << m << ": " << "NO" << endl;
		}
	}
	infile.close();
	myfile.close();
	return 0;
}
