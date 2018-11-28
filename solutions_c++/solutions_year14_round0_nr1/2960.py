//#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int t=0; t < T; t++) {
		int choice, temp;
		in >> choice;
		vector<int> options;
		for (int r=0; r < 4; r++) {
			for (int c=0; c < 4; c++) {
				in >> temp;
				if (r+1 == choice)
					options.push_back(temp);
			}
		}
		//----
		in >> choice;
		int count(0), answer;
		for (int r=0; r < 4; r++) {
			for (int c=0; c < 4; c++) {
				in >> temp;
				if (r+1 == choice) {
					for (size_t i = 0; i < options.size(); i++)
						if (options[i] == temp) {count++; answer = temp;}
				}
			}
		}
		out << "Case #" << t+1 << ": ";
		if (count == 0) out << "Volunteer cheated!\n";
		else if (count > 1) out << "Bad magician!\n";
		else out << answer << endl;
	}//case
}