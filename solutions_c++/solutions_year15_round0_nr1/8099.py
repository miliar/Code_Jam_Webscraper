#include <fstream>
#include <string>
using namespace std;

int main() {

	ifstream input("input.txt");
	ofstream output("output.txt");

	int T;
	input >> T;

	for (int t=1;t<=T;t++)
	{
		int l;
		input >> l;
		l++;
		int * people = new int[l];
		for (int i=0;i<l;i++)
			people[i] = 0;

		string data;
		input >> data;
		for (int i=0;i<l;i++) 
			people[i] = data[i] - '0';

		int need = 0;
		int standed = 0;
		for (int i=0;i<l;i++) {
			if (i > standed) {
				need += i - standed;
				standed = i;
			}
			standed += people[i];
		}
		output << "Case #" << t << ": " << need << endl;
		delete [] people;
	}
	output.close();
	system("PAUSE");
	return 0;
}