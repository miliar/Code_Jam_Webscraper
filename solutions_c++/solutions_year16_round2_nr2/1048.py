#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

bool matchp(string p, int num)
{
	char ss[10];
	sprintf(ss, "%03i", num);

	for (int i = 0; i < 3; ++i)
	{
		if (p[i] != '?' && ss[i] != p[i])
			return false;
	}
	return true;
}

void testcase()
{
	string sc, sj;
	string inp;
	cin >> sc >> sj;

	int len = max(sc.size(), sj.size());

	while (sc.size() < 3)
		sc = "0" + sc;

	while (sj.size() < 3)
		sj = "0" + sj;

	int mc = 1000, mj = 1000, mindiff = 1000;

	for( int i = 0 ; i < 1000 ; ++i)
		for (int j = 0; j < 1000; ++j)
		{
			if (abs(i - j) <= mindiff && matchp(sc,i) && matchp(sj,j))
				if ( abs(i - j) < mindiff || (abs(i - j) == mindiff && i < mc) || (abs(i - j) == mindiff && i == mc && j < mj))
				{
					mindiff = abs(i - j);
					mc = i;
					mj = j;
				}
		}

	char res[20];

	char format[20];

	sprintf(format, "%%0%ii %%0%ii", len, len);
	sprintf(res, format, mc, mj);
	cout << res << endl;
} 

int main()
{
  int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
    cout << "Case #" << i + 1 << ": ";
		testcase();
	}
	
	return 0;
}