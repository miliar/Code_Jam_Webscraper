#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char * argv[])
{
	ifstream in;
	in.open(argv[1]);
	ofstream out;
	out.open(argv[2]);
	int nCase;
	in >> nCase;
	for (int cas = 0; cas < nCase; cas++)
	{
		out << "Case #" << cas + 1 << ": ";
		int n, m;
		in >> n >> m;
		vector<vector<int> > a;
		a.resize(n);
		for (int i = 0; i < n; i++)
		{
			a[i].resize(m);
			for (int j = 0; j < m; j++)
				in >> a[i][j];
		}
		bool ok = true;
		for (int i = 0; i < n; i++)
		{
			bool allMin = true;
			int min = a[i][0];
			
			for (int j = 0; j < m; j++)
			{
				if (a[i][j] != min)
					allMin = false;
				if (a[i][j] < min)
					min = a[i][j];
			}
			if (!allMin)
				for (int j = 0; j < m; j++)
					if (a[i][j] == min)
					{
						for (int k = 0; k < n; k++)
							if (a[k][j] > min)
								ok = false;
					}
		}
		if (ok)
			out << "YES\n";
		else
			out << "NO\n";
	}
	in.close();
	out.close();
	return 0;
}
