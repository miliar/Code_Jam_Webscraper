#include <iostream>
#include <fstream>

#define DBG while(0)cout

using namespace std;

int main()
{
    //ifstream fin("input.txt", ios::in);
    ifstream fin("A-small-attempt0.in", ios::in);
    ofstream fout("output.txt", ios::out);

    int T;

    fin >> T;

    int r1, r2;
    int row1[4], row2[4];
    int temp;
    for (int nCase = 1; nCase <= T; ++nCase)
    {
	fin >> r1;
	DBG << r1 << endl;
	for (int r = 1; r <= 4; ++r)
	{
	    for (int c = 0; c < 4; ++c)
	    {
		if (r == r1)
		    fin >> row1[c];
		else
		    fin >> temp;
	    }
	}

	fin >> r2;
	DBG << r2 << endl;
	for (int r = 1; r <= 4; ++r)
	{
	    for (int c = 0; c < 4; ++c)
	    {
		if (r == r2)
		    fin >> row2[c];
		else
		    fin >> temp;
	    }
	}

	// compare
	int ans = 0;
	int count = 0;
	for (int c1 = 0; c1 < 4; ++c1)
	{
	    for (int c2 = 0; c2 < 4; ++c2)
	    {
		DBG << row1[c1] << " " << row2[c2] << endl;
		if (row1[c1] == row2[c2])
		{
		    ans = row1[c1];
		    ++count;
		} 
	    }
	}

	fout << "Case #" << nCase << ": ";
	if (count == 1)
	    fout << ans;
	else if (count > 1)
	    fout << "Bad magician!";
	else
	    fout << "Volunteer cheated!";
	fout << endl;
    }

    return 0;
}
