#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

#ifdef _DEBUG_
#define fin cin
#define fout cout
#else
//ifstream fin("A-small-attempt0.in.txt");
//ofstream fout("A-small-attempt0.out.txt");
ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");
#endif

const long long maxM = 1000000;
vector<bool> visited;

bool isAllVisited()
{
    bool ret = true;
    for (int i = 0; i < 10; ++i) ret &= visited[i];
    return ret;
}

void updateVisited(long long n)
{
    while (n > 0)
    {
	visited[n%10] = true;
	n /= 10;
    }
}

int main()
{
    int T;
    fin >> T;
    for (int c = 1; c <= T; ++c)
    {
	long long N;
	fin >> N;
	if (N == 0)
	{
	    fout << "Case #" << c << ": INSOMNIA" << endl;
	    continue;
	}
	visited = vector<bool>(10, false);
	long long m = 0;
	while(!isAllVisited())
	{
	    ++m;
	    updateVisited(m*N);
	    if (m >= maxM)
	    {
		fout << "Issue here!" << endl;
		break;
	    }
	}
	fout << "Case #" << c << ": " << m*N << endl;
    }
    
    return 0;
}
