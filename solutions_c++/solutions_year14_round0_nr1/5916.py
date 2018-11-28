#include <fstream>
#include <vector>
using namespace std;

int main() {

	ifstream input("input.txt");
	ofstream out("out.txt");
	vector<int> row1;
	vector<int> row2;
	int t;
	int rowc;
	int temp;
	input >> t;
	for (int i=0;i<t;i++) {
		input >> rowc;
		for (int a=0;a<(rowc-1)*4;a++) input >> temp;
		for (int x=0;x<4;x++) {input >> temp; row1.push_back(temp);}
		for (int a=0;a<(4-rowc)*4;a++) input >> temp;
		input >> rowc;
		for (int a=0;a<(rowc-1)*4;a++) input >> temp;
		for (int x=0;x<4;x++) {input >> temp; row2.push_back(temp);}
		for (int a=0;a<(4-rowc)*4;a++) input >> temp;
		int solution = -1;
		bool valid = false;
		for (int a=0;a<4;a++)
			for (int b=0;b<4;b++) {
				if (row1[a]==row2[b]) {
					if (!valid) {
						valid = true;
						solution = row1[a];
					}
					else {
						valid = false;
						a = 4;
						break;
					}
				}
			}
		if (valid) out << "Case #" << (i+1) << ": " << solution << endl;
		else if (solution == -1) out << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
		else out << "Case #" << (i+1) << ": Bad magician!" << endl;
		while (row1.size() > 0 ) row1.pop_back();
		while (row2.size() > 0 ) row2.pop_back();
	}
}