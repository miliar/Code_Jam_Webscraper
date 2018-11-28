#include <string>
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>

using namespace std;

unsigned long long doit(unsigned long long A,
			multiset<unsigned long long>::const_iterator beg,
			multiset<unsigned long long>::const_iterator end)
{
    if (beg == end)
    {
	return 0;
    }
    multiset<unsigned long long>::const_iterator next = beg;
    ++next;
    if (A > *beg)
    {
	return doit(A + *beg, next, end);
    }

    if (A == 1)
    {
	return 1 + doit(A, next, end);
    }
    else
    {
	unsigned long long dropCnt = doit(A, next, end) + 1;
	unsigned long long cnt = 0;
	unsigned long long newA = A;
	while(1)
	{
	    newA = newA * 2 - 1;
	    ++cnt;
	    if (newA > *beg)
	    {
		break;
	    }
	}
	unsigned long long addCnt = cnt + doit(newA, beg, end);
	return min(dropCnt, addCnt);
	// return 1 + min(doit(A + A - 1, beg, end),
	// 	       doit(A, next, end));
    }
}

int main (int argc, char*argv[])
{
    ifstream input("test.in");
    int x = 0;
    input >> x;
    unsigned long long a, n;
    int cnt = 0;
    for (int i = 0; i < x; ++i)
    {
	cnt = 0;
	input >> a >> n;
	multiset<unsigned long long> motes;
	for (int j = 0; j < n; ++j)
	{
	    unsigned long long v;
	    input >> v;
	    motes.insert(v);
	}
	unsigned long long res = doit (a, motes.begin(), motes.end());
	cout << "Case #" << i + 1 << ": ";
	cout << res;
	cout << std::endl;
    }
}
