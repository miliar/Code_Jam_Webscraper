#include <iostream>
#include <fstream>

using namespace std;

int main()
{
//    ifstream fin("input.txt", ios::in);
//    ifstream fin("B-small-attempt0.in", ios::in);
    ifstream fin("B-large.in", ios::in);
    ofstream fout("output.txt", ios::out);

    int N, R, C;
    fin >> N;

    int** lawn;
    for (int l = 0; l < N; ++l) // lawn
    {
	fin >> R >> C;
	lawn = new int*[R];

    	for (int r = 0; r < R; ++r)
	{
	    lawn[r] = new int[C];
	    for (int c = 0; c < C; ++c)
	    {
		fin >> lawn[r][c];
	    }
	}
/*
	cout << R << " x " << C << endl;
	for (int r = 0; r < R; ++r)
	{
	    for (int c = 0; c < C; ++c)
	    {
		cout << lawn[r][c];
	    }
	    cout << endl;
	}
	cout << endl;
*/
	int h;
	bool OK = true;
	bool rowOK = true;
	bool colOK = true;
	for (int r = 0; r < R; ++r)
	{
	    for (int c = 0; c < C; ++c)
	    {
		h = lawn[r][c];
		rowOK = true;
		colOK = true;

		// check row
		for (int c2 = 0; c2 < C; ++c2)
		{
		    if (lawn[r][c2] > h)
		    {
			rowOK = false;
			break;
		    }
		}
	    
		// check col
		for (int r2 = 0; r2 < R; ++r2)
		{
		    if (lawn[r2][c] > h)
		    {
			colOK = false;
			break;
		    }
		}

		if (rowOK == false && colOK == false)
		{
		    OK = false;
		    break;
		}
	    }
	    if (OK == false)
		break;
	
	}

	fout << "Case #" << l+1 << ": ";
	if (OK == true)
	    fout << "YES" << endl;
	else
	    fout << "NO" << endl;

	for (int r = 0; r < R; ++r)
	    delete lawn[r];
	delete lawn;
    }

    return 0;
}
