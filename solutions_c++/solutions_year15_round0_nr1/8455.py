#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;
	for (int t=1; t<=T; t++) {
		int Smax;
		fin >> Smax;
		
		int countFriends = 0, countClopMembers = 0;
		char countMembers[1001];

		fin >> countMembers[0];
		int members = (int)countMembers[0]- 48;
		if (!members) {
			countFriends++;
			countClopMembers++;
		} else {
			countClopMembers += members;
		}

		for (int shynessLevel = 1; shynessLevel <= Smax; shynessLevel++) {
			fin >> countMembers[shynessLevel];
			int members = (int)countMembers[shynessLevel] - 48;
			if (countClopMembers > shynessLevel) {
				countClopMembers += members;
			} else {
				if (members) {
					countClopMembers += members;
				} else {
					countFriends++;
					countClopMembers++;
				}
			}
		}
		fout << "Case #" << t << ": " << countFriends << endl;
	}
	fout.close();
	fin.close();
	return 0;
}