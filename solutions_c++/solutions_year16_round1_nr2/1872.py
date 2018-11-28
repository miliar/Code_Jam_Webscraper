#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <set>
#include <vector>
#include <sstream>

using namespace std;

int main() {
	ofstream ofile;
	ofile.open("./B.out");
	ifstream ifile;
	ifile.open("./B-small-attempt1.in");
	int t, tt, n, nn, i, num;
	tt = 0;
	unordered_map<int, int> dic;
	set<int> res;
	string s;
	stringstream iss;
	getline(ifile, s);
	iss << s;
	iss >> t;
	while(tt < t)
	{
		res.clear();
		dic.clear();
		iss.clear();
		getline(ifile, s);
		iss << s;
		iss >> n;
		nn = 0;
		while(nn < 2 * n - 1)
		{
			iss.clear();
			getline(ifile, s);
			iss << s;
			while(iss >> num)
				++dic[num];
			++nn;
		}
		for(auto iter = dic.begin(); iter != dic.end(); ++iter)
		{
			if(iter->second % 2 == 1)
			res.insert(iter->first);
		}
		ofile << "Case #" << tt + 1 << ": ";
		auto iter = res.begin();
		for(i = 0; i < res.size() - 1; ++iter, ++i)
		{
			 ofile << *iter << " ";
		}
		ofile << *iter << "\n";
		tt++;
	}
	ifile.close();
	ofile.close();
	return 0;
}