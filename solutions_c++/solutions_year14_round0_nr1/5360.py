#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iterator>
#include <set>
#include <limits>
#include <boost/smart_ptr/scoped_array.hpp>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("output.txt");

std::string calc(int a1, int a2, std::vector<int> &v1, std::vector<int> &v2)
{
	sort(v1.begin() + a1 * 4, v1.begin() + a1 * 4 + 4);
	sort(v2.begin() + a2 * 4, v2.begin() + a2 * 4 + 4);
	vector<int> vv;
	set_intersection(v1.begin() + a1 * 4,  v1.begin() + a1 * 4 + 4,
			v2.begin() + a2 * 4, v2.begin() + a2 * 4 + 4,
			back_inserter(vv));
	if(vv.empty()) return "Volunteer cheated!";
	if(vv.size() > 1) return "Bad magician!";
	ostringstream os;
	os << vv[0];
	return os.str();
}

int main()
{
	int T;
	fin >> T;
	fout << setprecision(7) << fixed;
	for(int i = 1; i <= T; ++i)
	{
		vector<int> v1(16), v2(16);
		int a1, a2;
		fin >> a1;
		for(int j = 0; j < 16; ++j) fin >> v1[j];
		fin >> a2;
		for(int j = 0; j < 16; ++j) fin >> v2[j];
		fout << "Case #" << i << ": " << calc(a1 - 1, a2 - 1, v1, v2) << std::endl;
	}
}
