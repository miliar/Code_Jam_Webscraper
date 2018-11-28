#include <iostream>
#include <string>
#include <vector>
#include <fstream>


using namespace std;

int main(int argc, char **argv)
{
	ifstream in(argv[1]);
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; i++){
		int nNum ;
		in >> nNum;
		string strDigits;
		in >> strDigits;
		vector<int> vecDigits;
		for (size_t j = 0; j < strDigits.size(); j++){
			vecDigits.push_back(strDigits[j]-'0');
		}
		int current = 0;
		int need = 0;
		for (size_t j = 0; j < vecDigits.size(); j++){
			if (vecDigits[j] > 0){
				if (current < j){
					need += (j-current);
					current = j;
				}
				current += vecDigits[j];
			}
		}
		cout<<"Case #"<<i+1<<": "<<need<<endl;
	}
	return 0;
}
