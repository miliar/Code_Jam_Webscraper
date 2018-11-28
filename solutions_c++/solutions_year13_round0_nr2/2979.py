#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>

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
    for (int i = 0; i < T; ++i)
    {
	int N, M;
	fin >> N;
	fin >> M;
	vector<vector<int> > L;
	L.resize(N);
	for (int j = 0; j < N; ++j)
	{
	    L[j].resize(M);
	    for (int k = 0; k < M; ++k)
	    {
		int in;
		fin >> in;
		L[j][k] = in;
	    }
	}
	bool can = true;
	for (int j = 0; j < N; ++j)
	{
	    for (int k = 0; k < M; ++k)
	    {
		bool row = true;
		bool col = true;

		for (int l = 0; l < M; ++l)
		    if(L[j][k] < L[j][l])
			row = false;
		for (int l = 0; l < N; ++l)
		    if(L[j][k] < L[l][k])
			col = false;

		can = can && (row || col);
	    }
	    
	}
	if (can)
	    fout << "Case #" << i+1 << ": YES" << endl;
	else
	    fout << "Case #" << i+1 << ": NO" << endl;
	    
    }
}
