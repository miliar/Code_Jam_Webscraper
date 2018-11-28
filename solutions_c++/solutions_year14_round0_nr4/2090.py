#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>
#include <stack>
#include <queue>
#include <set>
#include <string>
#include <iomanip>
#include <deque>

using namespace std;

#define PI 3.14159265358979323846

using namespace std;

void main()
{
	ifstream inp("E:\\Note\\Input.txt");
	cin.rdbuf(inp.rdbuf());
	ofstream outp("E:\\Note\\Output.txt");
	cout.rdbuf(outp.rdbuf());
	int t;
	cin >> t;
	for (int k = 0; k < t; k++){
		int n;
		cin >> n;
		vector<double> naiomi;
		vector<double> ken;
		vector<double> naiomi2;
		vector<double> ken2;
		for (int i = 0; i < n; i++)
		{
			double q;
			cin >> q;
			naiomi.push_back(q);
		}
		for (int i = 0; i < n; i++)
		{
			double q;
			cin >> q;
			ken.push_back(q);
		}
		sort(naiomi.begin(), naiomi.end());
		sort(ken.begin(), ken.end());
		naiomi2 = naiomi;
		ken2 = ken;
		int ans2 = 0;
		for (int i = 0; i < n; i++)
			if (naiomi.back()>ken.back()){
				ans2++;
				naiomi.pop_back();
				ken.erase(ken.begin());
			}
			else
			{
				int z = ken.size() - 1;
				while (z >= 0 && ken[z] > naiomi.back())
					z--;
				naiomi.pop_back();
				z++;
				ken.erase(ken.begin() + z);
			}
		int ans1 = 0;
		for (int i = 0; i < n; i++)
		{
			if (naiomi2.back()>ken2.back())
			{
				ans1++;
				int z = naiomi2.size() - 1;
				while (z >= 0 && naiomi2[z] > ken2.back())
					z--;
				z++;
				ken2.pop_back();
				naiomi2.erase(naiomi2.begin() + z);
			}
			else
			{
				naiomi2.erase(naiomi2.begin());
				ken2.pop_back();
			}
		}
		cout << "Case #" << k + 1 << ": " << ans1 << ' ' << ans2 << endl;
	}
}