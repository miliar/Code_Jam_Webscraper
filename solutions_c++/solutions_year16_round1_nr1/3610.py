#include <fstream>
#include <string>

using namespace std;

void resol(int i, ifstream & in, ofstream & out);

int main(){
	ifstream in; ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; ++i)
		resol(i, in, out);
	in.close();
	out.close();
	return 0;
}

void resol(int i, ifstream & in, ofstream & out){
	string str1, str2 = "";
	in >> str1;
	str2.push_back(str1.at(0));
	for (int j = 1; j < str1.size(); ++j){
		if (str1.at(j) < str2.at(0))
			str2.push_back(str1.at(j));
		else str2.insert(str2.begin(), str1.at(j));
	}
	out << "Case #" << i + 1 << ": " << str2 << '\n';
}