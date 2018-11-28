// errachete - A: Senate Evacuation

#include <fstream>
#include <iomanip>
#include <cctype>
#include <string>
#include <sstream>
#include <vector>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <utility>
#include <functional>
#include <ctime>
#include <cstdio>
#include <cstdlib>
using namespace std;

using sint = short int;
using lint = long int;
using llint = long long int;
using uint = unsigned int;
using usint = unsigned short int;
using ulint = unsigned long int;
using ullint = unsigned long long int;
using lfloat = long float;
using ldouble = long double;

ifstream fin;
ofstream fout;

ostream & operator<<(ostream & sal, vector< string > const& v)
{
	for (int i = 0; i < v.size(); ++i)
	{
		sal << ' ' << v[i];
	}
	return sal;
}

bool vectorNulo(vector< ullint > const& v)
{
	for (int i = 0; i < v.size(); ++i)
	{
		if (v[i] != 0)
			return false;
	}
	return true;
}
int maximo(vector< ullint > const& v)
{
	int max = v[0], pos = 0;
	for (int i = 1; i < v.size(); ++i)
	{
		if (v[i] > max)
		{
			max = v[i];
			pos = i;
		}
	}
	return pos;
}
bool mayoriaAbs(vector< ullint > const& v, int & pos)
{
	bool mayoria = false;
	for (int i = 0; i < v.size() && !mayoria; ++i)
	{
		ullint resto = 0;
		for (int j = 0; j < v.size(); ++j)
		{
			if (j != i)
				resto += v[j];
		}
		if (resto < v[i])
		{
			mayoria = true;
			pos = i;
		}
	}
	return mayoria;
}
void resolucion(int caso)
{
	vector< string > evacuacion;
	int numPartidos = 0;

	fin >> numPartidos;
	vector< ullint > senado(numPartidos);
	for (ullint & partido : senado)
		fin >> partido;

	while (!vectorNulo(senado))
	{
		int pos = maximo(senado);
		--senado[pos];
		string evacuado = "";
		evacuado.push_back(char(pos + int('A')));

		if (mayoriaAbs(senado, pos))
		{
			--senado[pos];
			evacuado.push_back(char(pos + int('A')));
		}

		evacuacion.push_back(evacuado);
	}

	fout << "Case #" << caso << ':' << evacuacion << '\n';
}

int main()
{
	fin.open("input.txt");
	fout.open("output.txt");

	int numCasos = 0;
	fin >> numCasos;
	for (int i = 0; i < numCasos; ++i)
		resolucion(i + 1);

	fin.close();
	fout.close();
	return 0;
}
