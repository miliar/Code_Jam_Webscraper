#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	if (in.is_open() && out.is_open())
	{
		string dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		int ts; in >> ts;
		for (int t = 1; t <= ts; ++t)
		{
			int n; in >> n;
			priority_queue<pair<int, int>, vector<pair<int, int> > > data;
			for (int i = 0; i < n; ++i)
			{
				int val; in >> val;
				data.push({val, i});
			}
			out << "Case #" << t << ":";
			while (!data.empty())
			{
				if (data.size() == 2)
				{
					pair<int, int> a = data.top();
					data.pop();
					pair<int, int> b = data.top();
					data.pop();
					if (a.first > 1) data.push({a.first - 1, a.second});
					if (b.first > 1) data.push({b.first - 1, b.second});
					out << " " << dict[a.second] << dict[b.second];
				}
				else
				{
					pair<int, int> a = data.top();
					data.pop();
					pair<int, int> b = data.top();
					if (a.first - b.first > 1)
					{
						if (a.first > 2) data.push({a.first - 2, a.second});
						out << " " << dict[a.second] << dict[a.second];
					}
					else if (a.first - b.first == 1)
					{
						data.pop();
						if (a.first > 1) data.push({a.first - 1, a.second});
						if (b.first > 1) data.push({b.first - 1, b.second});
						out << " " << dict[a.second] << dict[b.second];
					}
					else
					{
						if (a.first > 1) data.push({a.first - 1, a.second});
						out << " " << dict[a.second];
					}
				}
				cout << data.size() << endl;
			}
			out << "\n";
		}
	}
	else
	{
		cerr << "failed to open file\n";
	}
	return 0;
}
