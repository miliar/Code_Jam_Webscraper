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

#define IN_FILE "D:\\A-large.in"
#define OUT_FILE "D:\\code_jam_out.txt"

void func(ifstream& in, ofstream& out)
{
    int dig[10];
    for (int i = 0; i < 10; i++)
            dig[i] = 0;

    int cnt = 0;

    int N;
    in >> N;

    if (N == 0)
    {
        out << "INSOMNIA" << endl;
        return;
    }

    int cur = 0;
    do {
        cur += N;

        for (int tmp = cur; tmp > 0; tmp /= 10)
        {
            if (dig[tmp % 10] == 0)
                cnt++;
            dig[tmp % 10] = 1;
        }

    } while (cnt < 10);

    out << cur << endl;
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
