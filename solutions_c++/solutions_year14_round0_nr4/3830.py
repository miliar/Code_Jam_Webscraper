#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::vector<std::string> SplitString (std::string line, char delimeter)
{
	std::vector<std::string> result;

	int delIndex;
	while ((delIndex = line.find (delimeter)) != std::string::npos)
	{
		result.push_back (line.substr (0, delIndex));
		line = line.substr (delIndex + 1);
	}

	result.push_back (line);
	return result;
}

std::vector<std::pair<double, bool> > Naomi, Ken;

int GetKenLastActive ()
{
	int lastActive = Ken.size () - 1;
	while (!(Ken[lastActive].second)) --lastActive;

	return lastActive;
}

int FindSortedOptimalFor (int NaomiIndex)
{
	int firstActive = 0;
	while (!(Ken[firstActive].second)) ++firstActive;

	if (Ken[GetKenLastActive ()].first < Naomi[NaomiIndex].first) return firstActive;

	for (size_t i = 0; i < Ken.size (); ++i)
	{
		if (!Ken[i].second) continue;

		if (Ken[i] > Naomi[NaomiIndex])
		{
			return i;
		}
	}

	return firstActive;
}

int main ()
{
	std::ifstream input ("D-large.in");
	std::ofstream output ("D-large.out");
	std::string line;
	getline (input, line);
	size_t n = atoi (line.c_str ());
	
	for (size_t t = 0; t < n; ++t)
	{
		getline (input, line);
		int N = atoi (line.c_str ());

		Naomi.resize (N);
		Ken.resize (N);

		getline (input, line);
		std::vector<std::string> sublinesNaomi = SplitString (line, ' ');
		getline (input, line);
		std::vector<std::string> sublinesKen = SplitString (line, ' ');

		for (int i = 0; i < N; ++i)
		{
			Naomi[i].first = atof (sublinesNaomi[i].c_str ());
			Naomi[i].second = true;
			Ken[i].first = atof (sublinesKen[i].c_str ());
			Ken[i].second = true;
		}

		std::sort (Naomi.begin (), Naomi.end ());
		std::sort (Ken.begin (), Ken.end ());

		int deceitfulResult = 0, honestResult = 0;

		for (int i = 0; i < N; ++i)
		{
			int opt = FindSortedOptimalFor (i);
			Naomi[i].second = Ken[opt].second = false;

			if (Naomi[i].first > Ken[opt].first)
			{
				++honestResult;
			}
		}

		for (int i = 0; i < N; ++i)
		{
			Naomi[i].second = Ken[i].second = true;
		}
		
		int KenIndex = 0;
		for (int i = 0; i < N; ++i)
		{
			if (!Naomi[i].second) continue;

			while (!Ken[KenIndex].second) ++KenIndex;

			Naomi[i].second = false;

			if (Naomi[i].first > Ken[KenIndex].first)
			{
				++deceitfulResult;
				Ken[KenIndex].second = false;
			}
			else
			{
				Ken[GetKenLastActive ()].second = false;
			}
		}

		output << "Case #" << t + 1 << ": " << deceitfulResult << " " << honestResult << std::endl;
	}

	input.close ();
	output.close ();
	return 0;
}