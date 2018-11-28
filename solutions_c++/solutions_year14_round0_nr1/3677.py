#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int main(int argc, char *argv[])
{
    if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    

    

    for (int t = 0; t < T; ++t)
    {
	vector<vector<int> > M;
	vector<vector<int> > N;
	M.resize(4);
	N.resize(4);

	int x,y;

	fin >> x;

	for (int i = 0; i < 4; ++i)
	{
	    M[i].resize(4);
	    for (int j = 0; j < 4; ++j)
	    {
		fin >> M[i][j];
	    }
	}


	fin >> y;
	
	for (int i = 0; i < 4; ++i)
	{
	    N[i].resize(4);
	    for (int j = 0; j < 4; ++j)
	    {
		fin >> N[i][j];
	    }
	}

	vector<int> m = M[x-1];
	vector<int> n = N[y-1];

	vector<int> sol;

	for (int i = 0; i < 4; ++i)
	    for (int j = 0; j < 4; ++j)
	    {
		if (m[i]==n[j]) sol.push_back(m[i]);
	    }
	
	
	fout << "Case #" << t+1 << ": ";
	if (sol.size() == 1)
	    fout << sol[0] << endl;
	else if (sol.size() == 0)
	    fout << "Volunteer cheated!" << endl;
	else
	    fout << "Bad magician!" << endl;
	
    }
    return 0;
}
