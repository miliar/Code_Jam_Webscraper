#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>
#include <queue>
#include <cassert>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
#if _JOE_PC
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int ncase; cin >> ncase;
	
	for (int icase = 0; icase < ncase; icase++)
	{
		string bits;
		cin >> bits;
		int count = 0; bool minus = false, parity = 0;
		for (int i = bits.size() - 1; i >= 0; i--)
		{
			//is neg
			if ((bits[i] == '-' && !parity) || (bits[i] == '+'&& parity))
			{
			//	if (!minus)
				{
					count++;
			//		minus = true;
					parity = !parity;
				}
			}
			else
			{
				minus = false;
			}
		}
		cout << "Case #" << icase + 1 << ": " << count << endl;

	}
}