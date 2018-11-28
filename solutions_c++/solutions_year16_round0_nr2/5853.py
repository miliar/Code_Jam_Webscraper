// Errachete - B: Revenge of the Pancakes

#include <fstream>
#include <string>
using namespace std;

using lint = unsigned long long int;

ifstream fin;
ofstream fout;

void resolucion(int caso)
{
	int i = 0;
	lint sol = 0;
	string pancakes = "";

	fin >> pancakes;
	i = pancakes.size() - 1;
	while (i >= 0 && pancakes[i] == '+')
		--i;
	for (; i > 0; --i)
	{
		if (pancakes[i - 1] != pancakes[i])
			++sol;
	}
	if ((sol % 2 == 0 && pancakes[0] == '-') || (sol % 2 != 0 && pancakes[0] == '+'))
		++sol;

	fout << "Case #" << caso + 1 << ": " << sol << '\n';
}

int main()
{
	fin.open("input.txt");
	fout.open("output.txt");
	int numCasos = 0;
	fin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolucion(i);
	fin.close();
	fout.close();
	return 0;
}