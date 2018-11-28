/*
Programa creado por Alejandro Linarez Rangel.
Para la Google Code Jam
Problema A a resolver.
En ISO C++11.
*/
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <functional>
#include <utility>
#include <complex>
#include <bitset>
#include <fstream>
#include <sstream>
#include <tuple>
#include <regex>

using namespace std;

typedef unsigned long long int uent;
typedef long long int ent;

int main (int argc, const char* argv[])
{
	int T = 0;
	cin >> T;
	for(int cuenta = 1;cuenta <= T;cuenta++)
	{
		cout << "Case #" << cuenta << ": ";
		int DevoradasCaso1 = 0,DevoradasCaso2 = 0,MayorNegativo = 0,N = 0, M[1005];
		cin >> N;
		for(int i = 0;i < N;i++)
		{
			cin >> M[i];
		}
		for(int i = 0;i < (N - 1);i++)
		{
			int valor = M[i + 1] - M[i];
			if(valor < 0)
			{
				DevoradasCaso1 += abs(valor);
				if(abs(valor) > MayorNegativo)
				{
					MayorNegativo = abs(valor);
				}
			}
		}
		for(int i = 0;i < (N - 1);i++)
		{
			if(M[i] > MayorNegativo)
			{
				DevoradasCaso2 += MayorNegativo;
			}
			else
			{
				DevoradasCaso2 += M[i];
			}
		}
		cout << DevoradasCaso1 << " " << DevoradasCaso2 << endl;
	}
	return 0;
}
