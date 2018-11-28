#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("data.in");
	ofstream outfile;
	outfile.open("data.out");

	int T;
	infile>>T;

	for (int caseIndex = 1; caseIndex <= T; caseIndex++)
	{
		
		long long int a1, b1;
		infile>>a1>>b1;
		
		
		int ans = 0;
		for (int i = a1; i <= b1; i++)
		{
			vector<int> a;
			int a1 = i;
			bool add = true;
			while(a1 > 0)
			{
				a.push_back(a1%10);
				a1 = a1/10;
			}
			for (int j = 0; j < a.size(); j++)
			{
				if (a[j] != a[a.size()-j-1])
				{
					add = false;
					break;
				}
			}

			if (!add)
			{
				continue;
			}
			else
			{
				int s = sqrt(i);
				if (s*s == i)
				{
					int ts = s;
					vector<int> t;
					while(ts > 0)
					{
						t.push_back(ts%10);
						ts = ts/10;
					}
					bool addthis = true;
					for (int j = 0; j < t.size(); j++)
					{
						if (t[j] != t[t.size()-j-1])
						{
							addthis = false;
							break;
						}
					}
					if (addthis)
					{
						ans++;
					}


				}
			}
		}

		outfile<<"Case #"<<caseIndex<<": "<<ans<<endl;
		

	}

	infile.close();
	outfile.close();
	return 0;
}