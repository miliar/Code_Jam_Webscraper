#include <fstream>
#include <vector>
#include <algorithm>

int war_answer(std::vector< double > naomi, std::vector< double > ken)
{
	int res = 0;
	int n = naomi.size();
	for (int i = 0; i < n; ++i)
	{
		bool find_larger = false;
		int index = -1;
		for (int j = 0; j < ken.size(); ++j)
		{
			if (naomi[i] < ken[j])
			{
				find_larger = true;
				index = j;
				break;
			}
		}
		if (find_larger)
		{
			ken.erase(ken.begin() + index);
		}
		else
		{
			res++;
			ken.erase(ken.begin());
		}
	}
	return res;
}
int dwar_answer(std::vector< double > naomi, std::vector< double > ken)
{
	int res = 0;
	int n = naomi.size();
	int i = 0;
	int j = 0;
	while ( i != n && j != n)
	{
		if (naomi[i] > ken[j])
		{
			res++;
			i++;
			j++;
		}
		else
		{
			i++;
		}
	}
	return res;
}

int main()
{
	std::ifstream input_file("input.txt");
	std::ofstream out_file("output.txt");
	int T;
	input_file >> T;
	for (int t = 1; t <= T; ++t)
	{
		int n;
		input_file >> n;
		std::vector< double > naomi, ken;
		for (int i = 0; i < n; ++i)
		{
			double tmp;
			input_file >> tmp;
			naomi.push_back(tmp);
		}
		for (int i = 0; i < n; ++i)
		{
			double tmp;
			input_file >> tmp;
			ken.push_back(tmp);
		}
		out_file << "Case #" << t << ": ";
		std::sort(naomi.begin(), naomi.end());
		std::sort(ken.begin(), ken.end());
		int war_ans = war_answer(naomi, ken);
		int dwar = dwar_answer(naomi, ken);
		out_file << dwar << " " << war_ans;
		if (t != T)
			out_file << "\n";
	}
	input_file.close();
	out_file.close();
}