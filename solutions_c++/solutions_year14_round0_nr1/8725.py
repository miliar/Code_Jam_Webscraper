#include <iostream>
#include <fstream>
using namespace std;


int main()
{
  ifstream fin ("A-small-attempt1.in");
	if (!fin)  {
		return 1;
        }
	
	ofstream fout ("A-small-attempt.out");

	if (!fout)  {
		return 1;  
		}

	int testCases;

	fin >> testCases;

	if (testCases < 0 || testCases > 100)  // validation
		return 1;

	unsigned int let1 = 1;
	while (let1 <= testCases) {
		unsigned int answer_result1, answer_result2;
		
		fin >> answer_result1;
		
		
		if (answer_result1 < 0 || answer_result1 > 4)
			return 1;
			
		int a1[4][4], a2[4][4];
		
		for (int i = 0 ; i < 4 ; i++)
			for (int k = 0 ; k < 4 ; k++)
				fin >> a1[i][k];
		
		fin >> answer_result2;
		
		if (answer_result2 < 0 || answer_result2 > 4)
			return 1;

		for (int i = 0 ; i < 4 ; i++)
			for (int k = 0 ; k < 4 ; k++)
				fin >> a2[i][k];
		
		answer_result1--;
		answer_result2--;
		
		int f1[] = {a1[answer_result1][0], a1[answer_result1][1], a1[answer_result1][2], a1[answer_result1][3]};
		int f2[] = {a2[answer_result2][0], a2[answer_result2][1], a2[answer_result2][2], a2[answer_result2][3]};
		
		int i = 0, k = 0, occur_result=0,saved_result=0;
		bool error_exception= true;
		
		for (i = 0 ; i < 4 ; i++) {
			for (k = 0 ; k < 4 ; k++) {
				if (f1[i] == f2[k]) {
					occur_result++;
					if (occur_result == 1 && error_exception)
						saved_result = k;
					error_exception = false;
					break;
				}
			}	
		}

		if (occur_result == 1)
			fout << "Case #" << let1 << ": " << f2[saved_result] << endl;
		else if (occur_result > 1)
			fout << "Case #" << let1 << ": " << "Bad magician!" << endl;
		else if (occur_result == 0)
			fout << "Case #" << let1 << ": " << "Volunteer cheated!" << endl;
		let1++;
	}
	fout.close ();
	fin.close ();
	return 0;

}