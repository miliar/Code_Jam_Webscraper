#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> *naomi_war;
vector<double> *ken_war;
vector<double> *naomi_dwar;
vector<double> *ken_dwar;

int war(vector<double> &naomi, vector<double> &ken, int size)
{
	int score = 0;
	//vector<char> v(size * 2);
	//int n_idx = 0;
	//int k_idx = 0;
	bool find;

	for (int i = 0; i < size; i++)
	{
		find = false;
		for (int j = 0; j < size; j++)
		{
			if (ken[j] > naomi[i])
			{
				ken[j] = -1;
				find = true;
				break;
			}
		}
		if (!find)
		{
			for (int j = 0; j < size; j++)
			{
				if (ken[j] != -1)
				{
					ken[j] = -1;
					break;
				}
			}
			score++;
		}
	}

	return score;
}
int dwar(vector<double> &naomi, vector<double> &ken, int size)
{
	int score = 0;
	int naomi_idx = 0;
	int ken_idx = 0;
	vector<char> v(size *2);
	int k_l_idx = 0;
	int k_h_idx = size * 2 - 1;
	int n_l_idx = 0;
	int n_h_idx = size * 2 - 1;

	for (int i = 0; i < size * 2; i++)
	{
		if (naomi[naomi_idx] > ken[ken_idx])
		{
			v[i] = 'k';
			ken_idx++;
		}
		else
		{
			v[i] = 'n';
			naomi_idx++;
		}
	}

	for (k_l_idx = 0; v[k_l_idx] != 'k'; k_l_idx++) ;
	for (k_h_idx = size * 2 - 1; v[k_h_idx] != 'k'; k_h_idx--) ;
	for (n_l_idx = 0; v[n_l_idx] != 'n'; n_l_idx++) ;
	for (n_h_idx = size * 2 - 1; v[n_h_idx] != 'n'; n_h_idx--) ;

	for (int i = 0; i < size; i++)
	{
		if (n_h_idx > k_h_idx)
		{
			for (k_l_idx++; v[k_l_idx] != 'k'; k_l_idx++) ;
			for (n_h_idx--; v[n_h_idx] != 'n'; n_h_idx--) ;
			score++;
		}
	}

	return score;
}
int dwar2(vector<double> &naomi, vector<double> &ken, int size)
{
	int score = 0;
	bool find;

	for (int i = 0; i < size; i++)
	{
		find = false;
		for (int j = 0; j < size; j++)
		{
			if (naomi[j] > ken[i])
			{
				naomi[j] = -1;
				find = true;
				score++;
				break;
			}
		}
		if (!find)
		{
			for (int j = 0; j < size; j++)
			{
				if (naomi[j] != -1)
				{
					naomi[j] = -1;
					break;
				}
			}
		}
	}

	return score;
}

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
		int ns;
		input_file>>ns;
		naomi_war = new vector<double>(ns);
		ken_war = new vector<double>(ns);
		naomi_dwar = new vector<double>(ns);
		ken_dwar = new vector<double>(ns);

		for (int i = 0; i < ns; i++)
		{
			input_file>>(*naomi_war)[i];
		}
		for (int i = 0; i < ns; i++)
		{
			input_file>>(*ken_war)[i];
		}
		sort(naomi_war->begin(), naomi_war->end());
		sort(ken_war->begin(), ken_war->end());
		for (int i = 0; i < ns; i++)
		{
			(*naomi_dwar)[i] = (*naomi_war)[i];
			(*ken_dwar)[i] = (*ken_war)[i];
		}

		int war_score = war(*naomi_war, *ken_war, ns);
		int dwar_score = dwar2(*naomi_dwar, *ken_dwar, ns);

		output_file<<"Case #"<<n<<": "<<dwar_score<<' '<<war_score<<endl;

		delete naomi_war;
		delete ken_war;
		delete naomi_dwar;
		delete ken_dwar;
	}

	input_file.close();
	output_file.close();
	system("pause");
	return 0;
}