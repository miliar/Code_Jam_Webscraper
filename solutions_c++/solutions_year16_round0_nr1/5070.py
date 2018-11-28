#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <cctype>
#include <math.h>
#include <numeric>
#include <set>
#include <stack>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	unsigned nooftests;

	unsigned inpnum=0;	
	unsigned sleepnum=0;
	
	
	cin >> nooftests;

	for (unsigned i = 0; i < nooftests; ++i)
	{
		bool insomnia = false;
		cin >> inpnum;

		if (inpnum != 0)
		{
			set<char> finaldigs;
			unsigned runningno = inpnum;
			unsigned cnt = 1;

			while (true)
			{
				stringstream ssinp;
				ssinp << runningno;
				string strinp = ssinp.str();
				sort(strinp.begin(), strinp.end());
				string::iterator strnewend = unique(strinp.begin(), strinp.end());

				string shortenedstr = string(strinp.begin(), strnewend);

				for (size_t st = 0; st < shortenedstr.length(); ++st)
				{
					finaldigs.insert(shortenedstr[st]);

					if (finaldigs.size() == 10)
						break;
				}

				cnt += 1;
				if (finaldigs.size() == 10)
				{
					sleepnum = runningno;
					break;
				}
				else
				{
					runningno = cnt*inpnum;
				}
			}
		}
		else
		{
			insomnia = true;			
		}

		if (!insomnia)
			cout << "Case #" << i + 1 << ": " << sleepnum<<"\n";
		else
			cout << "Case #" << i + 1 << ": INSOMNIA"<<"\n";
	}

	return 0;
}