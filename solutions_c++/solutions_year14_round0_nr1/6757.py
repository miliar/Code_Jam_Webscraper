#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("small.in");
ofstream out("small.out");

void ReadAndGenerateNeedeRow(vector <int>& vec)
{
    vec.clear();
    int rowNumber, k;
    in >> rowNumber;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        {
            in >> k;
            if (i + 1 == rowNumber)
                vec.push_back(k);
        }
}

int main()
{
	int test, t;
	in >> test;
	for (t = 1; t <= test; ++t)
	{
        vector <int> A, B, C;
        ReadAndGenerateNeedeRow(A);
        ReadAndGenerateNeedeRow(B);
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        set_intersection(A.begin(), A.end(), B.begin(), B.end(), back_inserter(C));
        if (C.size() == 1)
            out << "Case #" << t << ": " << C[0] << endl;
        if (C.size() == 0)
            out << "Case #" << t << ": Volunteer cheated!" << endl;
        if (C.size() > 1)
            out << "Case #" << t << ": Bad magician!" << endl;
	}

	return 0;
}