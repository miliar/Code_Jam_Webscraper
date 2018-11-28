#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

//#define DEBUG

#ifdef DEBUG
ifstream fin("A.in");
ofstream fout("A.out");
#else
ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");
#endif

int main()
{
    int T; fin >> T;
    for(int c = 1; c <= T; c++)
    {
	fout << "Case #" << c << ": ";
	int N;
	vector<int> input;
	fin >> N;
	for(int i = 0; i < N; i++)
	{
	    int m; fin >> m;
	    input.push_back(m);
	}
	int ans1 = 0, ans2 = 0, maxGap = 0;
	for(int i = 0 ; i < N; i++)
	{
	    if(i > 0 && input[i] < input[i-1])
	    {
		ans1 += input[i-1]-input[i];
		maxGap = max<int>(maxGap, input[i-1]-input[i]);
	    }
	}
	for(int i = 0; i < N-1; i++)
	{
	    if(input[i] <= maxGap) ans2 += input[i];
	    else ans2 += maxGap;
	}
	fout << ans1 << " " << ans2 << endl;;
    }

    return 0;
}
