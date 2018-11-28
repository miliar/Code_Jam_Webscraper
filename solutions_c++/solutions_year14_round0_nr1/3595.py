#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> *v;
int arrange1[4][4];
int arrange2[4][4];
int row1_idx, row2_idx;
int result, result_count;

int main()
{
	ifstream input_file;
	ofstream output_file;
	string line;
	int case_num = 0;

	input_file.open("test.in");
	if (!input_file)
	{
		cout<<"No File \"test.in\" Found!"<<endl;
	}
	output_file.open("test.out");
	if (!output_file)
	{
		cout<<"No File \"test.out\" Created!"<<endl;
	}
	input_file>>case_num;
	cout<<"Num:"<<case_num<<endl;

	for (int n = 1; n <= case_num; n++)
	{
		int row = 0;
		
		input_file>>row;
		row1_idx = row - 1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				input_file>>arrange1[i][j];
			}
		}

		input_file>>row;
		row2_idx = row - 1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				input_file>>arrange2[i][j];
			}
		}

		v = new vector<int>(8);
		for (int i = 0; i < 4; i++)
		{
			(*v)[i * 2] = arrange1[row1_idx][i];
			(*v)[i * 2 + 1] = arrange2[row2_idx][i];
		}
		sort(v->begin(), v->end());

		result = result_count = 0;
		for (int i = 0; i < 7; i++)
		{
			if ((*v)[i] == (*v)[i+1])
			{
				result = (*v)[i];
				result_count++;
			}
		}

		output_file<<"Case #"<<n<<": ";
		switch (result_count)
		{
		case 0:
			output_file<<"Volunteer cheated!"<<endl;
			break;
		case 1:
			output_file<<result<<endl;
			break;
		default:
			output_file<<"Bad magician!"<<endl;
			break;
		}

		delete v;
	}

	input_file.close();
	output_file.close();
	system("pause");
	return 0;
}