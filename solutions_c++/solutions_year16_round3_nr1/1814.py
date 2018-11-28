#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

//#define _DEBUG_
#ifdef _DEBUG_
#define fin cin
#define fout cout
#else
//ifstream fin("A-small-attempt1.in.txt");
//ofstream fout("A-small-attemp1.out.txt");
ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");
#endif

int main()
{
    int T; fin >> T;
    for (int c = 1; c <= T; ++c)
    {
	int N; fin >> N;
	vector<int> P(N);
	int sum = 0;
	for (int i = 0; i < N; ++i)
	{	    
	    fin >> P[i];
	    sum += P[i];
	}
	fout << "Case #" << c << ":";
	while (sum > 0)
	{
	    // look for two max
	    int maxIdx1 = -1, maxIdx2 = -1;
	    if (P[0] > P[1])
	    {
		maxIdx1 = 0;
		maxIdx2 = 1;
	    }
	    else
	    {
		maxIdx1 = 1;
		maxIdx2 = 0;
	    }
	    for (int i = 2; i < N; ++i)
	    {
		if (P[i] > P[maxIdx1]) maxIdx1 = i;
		else if (P[i] > P[maxIdx2]) maxIdx2 = i;
	    }
	    // sent two out
	    if (sum != 3 && P[maxIdx1] > 0 && P[maxIdx2] > 0)
	    {
		char c1 = 'A' + maxIdx1;
		char c2 = 'A' + maxIdx2;
		fout << " " << c1 << c2;
		sum -= 2;
		P[maxIdx1]--; P[maxIdx2]--;
	    }
	    else // send one out
	    {
		char c1 = 'A' + maxIdx1;
		fout << " " << c1;
		sum--; P[maxIdx1]--;
	    }
	    // check for bug
	    for (int i = 0; i < N; ++i)
	    {
		if (sum > 0 && (P[i] / sum - 1/2 > 0))
		{
		    cout << "Error at: " << c << endl;
		    cout << P[i] << "/" << sum << endl;
		}
	    }
	}
	fout << endl;
    }
    return 0;
}
