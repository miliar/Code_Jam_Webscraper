#include <iostream>
#include <fstream>
#include <set>

int main()
{
	std::ifstream input_file("input.txt");
	std::ofstream out_file("output.txt");
	int T;
	input_file >> T;
	for (int t = 1; t <= T; ++t)
	{
		int arr[4][4];
		int x1;
		input_file >> x1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				input_file >> arr[i][j];
		std::set< int > s1;
		for (int i = 0; i < 4; i++)
			s1.insert( arr[x1-1][i] );
		int x2;
		input_file >> x2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				input_file >> arr[i][j];
		std::set< int > s2;
		for (int i = 0; i < 4; i++)
			s2.insert( arr[x2-1][i] );
		int count = 0;
		int c = 0;
		for (auto it = s1.cbegin(); it != s1.cend(); ++it)
		{
			count += s2.count( *it );
			if (s2.count( *it ) > 0)
				c = *it;
		}
		out_file << "Case #" << t << ": ";
		if (count == 0)
			out_file << "Volunteer cheated!";
		else if (count == 1)
			out_file << c;
		else
			out_file << "Bad magician!";
		if (t != T)
			out_file << "\n";
	}
	out_file.close();
	input_file.close();
	return 0;
}