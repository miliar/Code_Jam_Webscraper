// Errachete - A: Counting ships

#include <fstream>
#include <vector>
using namespace std;

using lint = unsigned long long int;

ifstream fin;
ofstream fout;

bool algoFalso(vector< bool > const& cifras)
{
	for (int i = 0; i < cifras.size(); ++i)
	{
		if (cifras[i] == false)
			return true;
	}
	return false;
}
void comprobar(vector< bool > & cifras, lint num)
{
	while (num != 0)
	{
		cifras[num % 10] = true;
		num /= 10;
	}
}

void resolucion(int caso)
{
	int N = 0;
	lint num = 0, i = 1;
	vector< bool > cifras(10, false);

	fin >> N;
	while (algoFalso(cifras) && N != 0)
	{
		num = N * i;
		comprobar(cifras, num);
		++i;
	}


	fout << "Case #" << caso + 1 << ": ";
	if (N == 0)
		fout << "INSOMNIA\n";
	else
		fout << num << '\n';
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