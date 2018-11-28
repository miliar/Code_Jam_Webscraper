#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<iomanip>
#include<algorithm>
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
	vector<double> n;
	vector<double> k;

	int N;
	fin >> N;

	n.resize(N);
	k.resize(N);


	for (int i = 0; i < N; ++i)
	    fin >> n[i];
	for (int i = 0; i < N; ++i)
	    fin >> k[i];

	sort(n.begin(),n.end());
	sort(k.begin(),k.end());

//	for (int i = 0; i < N; ++i)
//	    cout << n[i] << " ";

	int I, J;

	int nW, nDW;
	nW = 0;
	nDW = 0;

	I = 0;
	J = 0;
	while (I != N && J != N)
	{
	    if (n[I] == k[J])
	    {
		++I;
	    }
	    else if(n[I] > k[J])
	    { 
		++I; 
		++J;
	        ++nDW;	
	    }
	    else if(n[I] < k[J])
	    {
		++I;
	    }
	}
	
	I = 0;
	J = 0;
	while (I != N && J != N)
	{
	    if (n[I] == k[J])
	    {
		++J;
	    }
	    else if(n[I] < k[J])
	    { 
		++I; 
		++J;
	        ++nW;	
	    }
	    else if(n[I] > k[J])
	    {
		++J;
	    }
	}

	for (int i = 0; i < N; ++i)
	{
	    for (int j = 0; j < N; ++j)
	    {
		
		
	    }
	}

	fout << "Case #" << t+1 << ": ";
	fout << nDW << " " << N-nW << endl;
	
    }
    return 0;
}
