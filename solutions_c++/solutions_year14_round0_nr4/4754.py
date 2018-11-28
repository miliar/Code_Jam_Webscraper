#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool doublecomp(double i, double j) 
{
    return i < j;
}

int main()
{
    int ncases;
    cin >> ncases;

    for (int i = 0; i < ncases; i++)
    {
	int nblocks;
	cin >> nblocks;

	vector<double> nablocks;
	vector<double> kblocks;

	for (int j = 0; j < nblocks; j++)
	{
	    double weight;
	    cin >> weight;
	    nablocks.push_back(weight);	    
	}
	for (int j = 0; j < nblocks; j++)
	{
	    double weight;
	    cin >> weight;
	    kblocks.push_back(weight);
	}

	sort(nablocks.begin(), nablocks.end(), doublecomp);
	sort(kblocks.begin(), kblocks.end(), doublecomp);

	int warpts = 0;
	int k = 0;
	for(int n = 0; n < nablocks.size(); n++)
	{
	    while(nablocks[n] > kblocks[k])
	    {
		k++;
		if (k >= kblocks.size()) break;
	    }
	    if(k >= kblocks.size()-1)
	    {
		warpts += (k-n);
		break;
	    }
	    k++;
	}

	int kwarpts = 0;
	int n = 0;
	for (int k = 0; k < kblocks.size(); k++)
	{
	    while(kblocks[k] > nablocks[n])
	    {
		n++;
		if(n >= nablocks.size()) break;
	    }
	    if(n >= nablocks.size()-1)		
	    {
		kwarpts += (n-k);
		break;
	    }
	    n++;
	}
	int dwarpts = nblocks - kwarpts;

	cout << "Case #" << i+1 << ": " << dwarpts << " " << warpts << endl;

    }
    return 0;
}

