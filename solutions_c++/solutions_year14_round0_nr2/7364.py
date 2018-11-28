#include <Windows.h>
#include <stdio.h>
#include <iostream>

using namespace std;
void solve()
{
	int max_cases = 0;
	cin >> max_cases;
	for(int icase = 0; icase < max_cases; icase++)
	{
		double c = 0, f = 0, x = 0;
		cin >> c;
		cin >> f;
		cin >> x;

		double max_seconds = 0;
		double min_seconds = 0;
		max_seconds = x / 2;
		min_seconds = max_seconds;
		double total_seconds = 0;
		double cf = 2;
		while(true)
		{
			double farm_seconds = c / cf;
			cf += f;
			double sec_req = total_seconds + farm_seconds + x / cf;
			if(sec_req > min_seconds)
			{
				break;
			}

			min_seconds = sec_req;
			total_seconds += farm_seconds;
		}

		printf("Case #%d: %0.7f\n", icase+1, min_seconds);
	}
}
int main(int argc, char *argv[])
{
	bool bclose_stdin = false, bclose_stdout = false;
	if(argc > 1)
	{
			freopen(argv[1], "r", stdin);
			bclose_stdin = true;
	}
	if(argc > 2)
	{
			freopen(argv[2], "w", stdout);
			bclose_stdout = true;
	}

	solve();

	if(bclose_stdin)
	{
		fclose(stdin);
	}
	if(bclose_stdout)
	{
		fclose(stdout);
	}

	return 0;
}