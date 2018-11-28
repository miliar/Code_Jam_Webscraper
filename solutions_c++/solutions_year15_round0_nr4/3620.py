#include <iostream>
#include <fstream>

int main()
{
	std::ifstream fin("D-small-attempt0.in");

	if(!fin){
		std::cout << "No good...\n";
		exit(1);
	}

	std::ofstream fout("SolvedProblemD.txt");

	int t;
	fin >> t;

	int x;
	int r;
	int c;

	for(int i=0; i<t; ++i){
		fin >> x;
		fin >> r;
		fin >> c;

		int times = r*c;

		if(x > 6)
			fout << "Case #" << i+1 << ": " << "RICHARD\n";

		if(times%x != 0){
			fout << "Case #" << i+1 << ": " << "RICHARD\n";
			continue;
		}

		if(x > r  && x > c){
			fout << "Case #" << i+1 << ": " << "RICHARD\n";
			continue;
		}

		if(x <= r && x-1 > c){
			fout << "Case #" << i+1 << ": " << "RICHARD\n";
			continue;
		}

		if(x-1 > r && x <= c){
			fout << "Case #" << i+1 << ": " << "RICHARD\n";
			continue;
		}

		fout << "Case #" << i+1 << ": " << "GABRIEL\n";

	}

	fout.close();


	return 0;
}