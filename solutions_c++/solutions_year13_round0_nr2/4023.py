#include <fstream>
#include <map>

typedef unsigned long long ull;
typedef long long ll;

#define FN "gcj1b"

using namespace std;

int main()
{
	ifstream in(FN ".in");
	ofstream out(FN ".out");

	int t;
	in >> t;

	int data[100][100];

	for(int i = 0; i < t; i++)
	{
		multimap<int,pair<int,int>> pts;

		int n,m;
		in >> n >> m;
		bool gcan = true;
		for(int j = 0; j < n; j++)
			for(int k = 0; k < m; k++)
			{
				int a;
				in >> a;
				data[j][k] = a;
				pts.insert(make_pair(a,make_pair(j,k)));
			}

		for(auto it = pts.begin(); it != pts.end(); ++it)
		{
			int cv = it->first;
			bool can = true;
			//check row
			for(int j = 0; j < n; j++)
			{
				if(data[j][it->second.second] > cv)
				{
					can = false;
					break;
				}
			}
			if(!can)
			{
				can = true;
				for(int k = 0; k < m; k++)
				{
					if(data[it->second.first][k] > cv)
					{
						can = false;
						break;
					}
				}
			}
			if(!can)
			{
				gcan = false;
				break;
			}
		}
		out << "Case #" << i+1 << (gcan ? ": YES\n" : ": NO\n");

	}

	out.close();
	return 0;
}