#include <string>
#include <iostream>
#include <fstream>

using namespace std;

bool isP(unsigned long long val)
{
    unsigned long long tmp = val;
    unsigned long long res = 0;
    while (tmp)
    {
	res = (res * 10) + (tmp % 10);
	tmp = tmp / 10;
    }
    //cout << "val: " << val << " rev: " << res << endl;
    if (val == res)
    {
	return true;
    }
    return false;
}

int main (int argc, char*argv[])
{
    ifstream input("C-small-attempt1.in");
    ofstream output("out.txt");
    int x = 0;
    input >> x;
    unsigned long long n, m;
    int cnt = 0;
    for (int i = 0; i < x; ++i)
    {
	cnt = 0;
	input >> n >> m;
	cout << n << ":" << m << endl;
	for (int j = 1; j <= m; ++j)
	{
	    if (j * j < n)
	    {
		continue;
	    }
	    if (j * j > m)
	    {
		break;
	    }
	    if (isP(j) && isP(j * j))
	    {
		cout << "found: " << j << ":" << j * j << endl;
		++cnt;
	    }
	}
	output << "Case #" << i + 1 << ": ";
	output << cnt;
	output << std::endl;
    }
}
