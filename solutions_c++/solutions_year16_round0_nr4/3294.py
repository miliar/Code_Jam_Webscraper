#include <string>
#include <fstream>
#include <iostream>

using namespace std;



int main()
{
	ifstream f;
	f.open("D-small-attempt0.in", ios::in);

	int t;
	f >> t;

	for (int i = 0; i < t; i++)
	{
		int k, c, s;
		f >> k >> c >> s;
		
		std::cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < k; j++) std::cout << j + 1 << ' ';
		std::cout << endl;
	}
	return 0;
}