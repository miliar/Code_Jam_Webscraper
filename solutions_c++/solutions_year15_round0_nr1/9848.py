#include <iostream>
#include <fstream>
#include <string>

int main()
{
	std::ifstream fin("A-small-attempt2.in");

	if(!fin){
		std::cout << "No good...\n";
		exit(1);
	}

	std::ofstream fout("Solved.txt");

	int t;
	fin >> t;

	char test;

	for(int i=0; i<t; ++i){
		int smax;

		fin.get(test);
		while(test == ' ' || test == '\n'){
			fin.get(test);
		}

		smax = test-'0';

		int peopleshy = 0;
		int totalpeople = 0;
		int need = 0;

		for(int j=0; j<smax+1; ++j){
			fin.get(test);
			while(test == ' ' || test == '\n'){
				fin.get(test);
			}

			peopleshy = test-'0';

			if(j > totalpeople){
				need += (j - totalpeople);
				totalpeople += (j-totalpeople);
			}

			totalpeople += peopleshy;
		}

		fout << "Case #" << i+1 << ": " << need << '\n';
	}

	fout.close();


	return 0;
}