#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<cmath>
#include<string>
#include<climits>
#include<stack>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main(){
	int T;
	int A;
	int temp;
	int ans;
	int matches = 0;
	vector <int> comp;

	fin >> T;
	for (int k = 0; k < T; k++){
		matches = 0;
		comp.clear();
		fin >> A;

		for (int p = 0; p < 4 * (A - 1); p++)
			fin >> temp;
		
		for (int l = 0; l < 4; l++)
		{
			fin >> temp;
			comp.push_back(temp);
		}

		for (int p = 0; p < 4 * (4-A); p++)
			fin >> temp;

		fin >> A;

		for (int p = 0; p < 4 * (A - 1); p++)
			fin >> temp;

		for (int l = 0; l < 4; l++)
		{
			fin >> temp;
			for (int s = 0; s < comp.size(); s++)
				if (temp == comp[s]){ 
					matches++; 
					ans = temp;
				}
		}

		for (int p = 0; p < 4 * (4 - A); p++)
			fin >> temp;

		if (matches == 0){ fout << "Case #" << k +1<< ": Volunteer cheated!" << endl; }
		if (matches == 1){ fout << "Case #" << k+1 << ": "<<ans<< endl; }
		if (matches >1){ fout << "Case #" << k +1<< ": Bad magician!" << endl; }

	}




	return 0;
}