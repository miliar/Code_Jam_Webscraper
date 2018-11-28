#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#define DBG while(0)cout

using namespace std;

int main()
{
    //ifstream fin("input.txt", ios::in);
    //ifstream fin("D-small-attempt0.in", ios::in);
    ifstream fin("D-large.in", ios::in);
    ofstream fout("output.txt", ios::out);

    int T;
    int B;

    fin >> T;

    for (int nCase = 1; nCase <= T; ++nCase)
    {
	fin >> B;
	vector<double> blocksN;
	vector<double> blocksK;
	vector<bool> usedN;
	vector<bool> usedK;
	double temp;

	for (int b = 0; b < B; ++b)
	{
	    fin >> temp;
	    blocksN.push_back(temp);
	    usedN.push_back(false);
	}
	for (int b = 0; b < B; ++b)
	{
	    fin >> temp;
	    blocksK.push_back(temp);
	    usedK.push_back(false);
	}

	sort(blocksN.begin(), blocksN.end());
	sort(blocksK.begin(), blocksK.end());

	int Nwin1 = 0;
	for (int bk = 0; bk < B; ++bk)
	{
	    if (usedK[bk] == true) continue;

	    bool foundn = false;
	    for (int bn = 0; bn < B; ++bn)
	    {
		if (usedN[bn] == true) continue;

		if (blocksN[bn] > blocksK[bk])
		{
		    usedN[bn] = true;
		    usedK[bk] = true;
		    foundn = true;
		    Nwin1++;
		    break;
		}
		
	    }
	    if (foundn == false)
	    {
		for (int bn = 0; bn < B; ++bn)
		{
		    if (usedN[bn] == true) continue;

		    usedN[bn] = true;
		    usedK[bk] = true;
		    break;
		}
	    }
	}

	int Nwin2 = 0;
	for (int bn = 0; bn < B; ++bn)
	    usedN[bn] = false;
	for (int bk = 0; bk < B; ++bk)
	    usedK[bk] = false;
	for (int bn = 0; bn < B; ++bn)
	{
	    if (usedN[bn] == true) continue;

	    bool foundk = false;
	    for (int bk = 0; bk < B; ++bk)
	    {
		if (usedK[bk] == true) continue;

		if (blocksK[bk] > blocksN[bn])
		{
		    usedN[bn] = true;
		    usedK[bk] = true;
		    foundk = true;
		    break;
		}
		
	    }
	    if (foundk == false)
	    {
		for (int bk = 0; bk < B; ++bk)
		{
		    if (usedK[bk] == true) continue;

		    usedN[bn] = true;
		    usedK[bk] = true;
		    break;
		}

		Nwin2++;
	    }
	}
	
	DBG << endl;
	fout << "Case #" << nCase << ": " << Nwin1 << " " << Nwin2 << endl;
    }

    return 0;
}
