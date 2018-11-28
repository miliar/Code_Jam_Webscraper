#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc,const char* argv[])
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("Standing_output.txt",'w');

	int num;
	int smax;
	string shylist;
	fin >> num;
	cout << num << endl;
	for (int i = 0; i < num; i++){
		int aud = 0;
		int achlevel = 0;
		fout << "Case #" << i + 1 << ": ";
		fin >> smax;
		fin >> shylist;
		for (int j = 0; j < shylist.size(); j++){
			if (j > achlevel){
				aud += j - achlevel;
				achlevel = j;
			}
			achlevel += int(shylist[j] - '0');
		}
		fout << aud << "\n";
	}
	fout << endl;
	fin.close();
	fout.close();
	return 0;
}
