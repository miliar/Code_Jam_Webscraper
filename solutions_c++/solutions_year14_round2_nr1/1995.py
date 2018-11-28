#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream cin("A-small-attempt1.in");
ofstream cout("output.txt");

bool good = true;
void win()
{
	cout << "Fegla Won" << endl;
	good = false;
}
int main()
{

	int t;
	cin >> t;
	for (int l = 1; l <= t ; ++l)
	{
		int n;
		cin >> n;
		vector<string> a(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		cout << "Case #" << l << ": ";
		good = true;
		long long count = 0;
		for (int i = 1; i < n && good; ++i)
		{
			
			int indf=0, inds=0;
			while (indf < a[i - 1].length() || inds < a[i].length())
			{
				if (a[i - 1][indf] != a[i][inds])
				{
					if (indf > 0 && a[i - 1][indf - 1] == a[i][inds])
					{
						count++;
						indf--;
					}
					else if (inds > 0 && a[i - 1][indf] == a[i][inds - 1])
					{
						count++;
						inds--;
					}					
					else
					{
						win();
						break;
					}
				}
				indf++;
				inds++;
			}
			
		}
		if (good)
			cout << count << endl;
	}
}