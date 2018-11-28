#include <iostream>
#include <vector>

using namespace std;

int get_old_score(vector<double>& nao, vector<double>& ken)
{
	vector<double> temp_nao = nao;
	vector<double> temp_ken = ken;
	int score = 0;
	for (int i = 0; i < temp_nao.size(); i++)
	{
		int size = temp_ken.size();
		for (vector<double>::iterator iter = temp_ken.begin(); iter != temp_ken.end(); ++iter)
		{
			if (*iter > temp_nao[i])
			{
				temp_ken.erase(iter);
				break;
			}
		}

		if (size == temp_ken.size())
		{
			temp_ken.erase(temp_ken.begin());
			++score;
		}
	}

	return score;
}

int get_new_score(vector<double>& nao, vector<double>& ken)
{
	vector<double> temp_nao = nao;
	vector<double> temp_ken = ken;
	int score = 0;
	sort(temp_ken.begin(), temp_ken.end(), greater<double>());

	for (int i = 0; i< temp_ken.size(); i++)
	{
		int size = temp_nao.size();
		for (vector<double>::iterator iter  = temp_nao.begin(); iter!=temp_nao.end(); ++iter)
		{
			if (*iter > temp_ken[i])
			{
				++score;
				temp_nao.erase(iter);
				break;
			}
		}

		if (size == temp_nao.size())
		{
			temp_nao.erase(temp_nao.begin());
		}
	}

	return score;
}

int main(void)
{
	int cases;
	cin >> cases;
	int blocks;

	vector<double> nao;
	vector<double> ken;

	double nao_block;
	double ken_block;

	for (int i = 0; i < cases; i++)
	{
		cin >> blocks;
		for (int j = 0; j < blocks; j++)
		{
			cin >> nao_block;
			nao.push_back(nao_block);
		}

		for (int j = 0; j < blocks; j++)
		{
			cin >> ken_block;
			ken.push_back(ken_block);
		}

		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());

		int old_score = get_old_score(nao, ken);
		int new_score = get_new_score(nao, ken);
		nao.clear();
		ken.clear();

		cout << "Case #" << i+1 << ": " << new_score << " " << old_score << endl;
	}
	return 0;
}
