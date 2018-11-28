#include <algorithm>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define IN_FILE "D:\\B-large.in"
#define OUT_FILE "D:\\code_jam_out.txt"

void func(ifstream& in, ofstream& out)
{
    string S;
    in >> S;

    int res = S[S.size() - 1] == '-' ? 1 : 0;

    for (int i = 1; i < S.size(); i++)
        res += S[i] != S[i - 1] ? 1 : 0;

    out << res << endl;
}

int main()
{
	ifstream in;
	in.open(IN_FILE);

	ofstream out;
	out.open (OUT_FILE);
	//out << fixed << showpoint << setprecision(7);

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		//cout << "Case #" << t << endl;
		out << "Case #" << t << ": ";
		func(in, out);
	}

	in.close();
	out.close();

	return 0;
}
