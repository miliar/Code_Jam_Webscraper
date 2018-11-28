#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

string magictrick(int r1, int r2, vector<int> v1, vector<int> v2)
{
	vector<int> v(v1.begin()+(r1-1)*4, v1.begin()+r1*4);
	v.insert(v.end(), v2.begin()+(r2-1)*4, v2.begin()+r2*4);
	sort(v.begin(), v.end());
	int len = v.size(), n = 0, tmp;
	for (int i = 0; i < len-1; ++i)
	{
		if (v[i]==v[i+1])
		{
			++n;
			tmp = v[i];
		}
	}
	if (n == 0)
		return "Volunteer cheated!";
	else if (n == 1)
	{
		stringstream ss;
		ss << tmp;
		return ss.str();
	}
	else
		return "Bad magician!";
}

int main(int argc, char* argv[])
{
	ifstream in("A-small-attempt0.in");
	ofstream out("result.txt");
	int T, a1, a2;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		in >> a1;
		vector<int> v1(16, 0), v2(16, 0);
		for (int j = 0; j < 16; ++j)
		{
			in >> v1[j];
		}
		in >> a2;
		for (int j = 0; j < 16; ++j)
		{
			in >> v2[j];
		}
		out << "Case #" << i+1 << ": " << magictrick(a1,a2,v1,v2) << endl;
	}

	in.close();
	out.close();
	return 0;
}