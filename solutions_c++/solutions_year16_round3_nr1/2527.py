#include <iostream>
#include <fstream>
#include <list>

using namespace std;

class Party {
public:
	Party(char name, int num) : mName(name), mNum(num) {};
	char mName;
	int mNum;
};

bool _compare(const Party* first, const Party* second) {
	if (first->mNum < second->mNum) {
		return false;
	}

	return true;
}

int main(int argc, char** argv) {
	int CASE_NUM = 0;

	// open input file
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");

	// load case number
	fin >> CASE_NUM;
	cout << "Case number : " << CASE_NUM << endl;

	//CASE_NUM = 3;
	for (int ti = 1; ti <= CASE_NUM; ti++) {
		int N = 0;
		int total = 0;
		fin >> N;

		cout << "N : " << N << endl;

		list<Party*> parties;
		char name = 'A';
		for (int i = 0; i < N; i++, name++) {
			int temp = 0;
			fin >> temp;
			parties.push_back(new Party(name, temp));
			total += temp;
		}

		fout << "Case #" << ti << ": ";

		while (total > 3) {
			parties.sort(_compare);
			list<Party*>::iterator iter = parties.begin();
			list<Party*>::iterator first = iter;
			iter++;
			list<Party*>::iterator second = iter;

			fout << (*first)->mName << (*second)->mName << " ";

			(*first)->mNum--;
			(*second)->mNum--;

			if ((*first)->mNum == 0)
				parties.erase(first);
			if ((*second)->mNum == 0)
				parties.erase(second);

			total -= 2;
		}

		parties.sort(_compare);

		if (total == 3) {
			list<Party*>::iterator first = parties.begin();

			fout << (*first)->mName << " ";
			(*first)->mNum--;

			if ((*first)->mNum == 0)
				parties.erase(first);

			total--;
		}

		list<Party*>::iterator iter = parties.begin();
		list<Party*>::iterator first = iter;
		iter++;
		list<Party*>::iterator second = iter;
		fout << (*first)->mName << (*second)->mName << endl;
	}

	fin.close();
	fout.close();
}
