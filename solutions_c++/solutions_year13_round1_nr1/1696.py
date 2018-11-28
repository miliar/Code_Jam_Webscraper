#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int main()
{
	std::ifstream file("A-small-attempt0 (3).in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	int nb;
	file >> nb;

	for(int i = 0; i < nb; ++i)
	{
		long long t,r;

		file >> r;
		file >> t;

		long long white_radius = r;
		long long radius = r +1; 
		long long resultat = 0;

		for(;;)
		{
			long long res = (radius * radius) - (white_radius* white_radius);

			if(t < res) break;
			else t -= res;

			resultat++;
			radius += 2;
			white_radius += 2;
		}
		file2 << "Case #" << i + 1 << ": " << resultat << std::endl;
	}
}