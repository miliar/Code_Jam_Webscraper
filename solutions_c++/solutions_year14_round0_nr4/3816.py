#include <fstream>
#include <set>
using namespace std;

int main()
{
	ifstream in("D-large (1).in");
	ofstream out("D.out");
	int t;
	in >> t;
	int n;
	for (int II = 1; II <= t; II++)
	{
		in >> n;
		set<double> a, b;
		double qq;
		for (int i = 0; i < n; i++)
		{
			in >> qq;
			a.insert(qq);
		}
		for (int i = 0; i < n; i++)
		{
			in >> qq;
			b.insert(qq);
		}

		set<double> aa(a);
		set<double> bb(b);

		pair<int, int> r1 = make_pair(0, 0);
		pair<int, int> r2 = make_pair(0, 0);
		for (auto it = a.end(); it != a.begin();)
		{
			it--;
			auto qt = b.lower_bound(*it);
			if (qt == b.end())
			{
				r1.first++;
				a.erase(it);
				it = a.end();
				b.erase(b.begin());
			}
			else
			{
				r1.second++;
				a.erase(it);
				it = a.end();
				b.erase(qt);
			}
		}

		a = aa;
		b = bb;

		for (auto it = a.begin(); it != a.end();)
		{
			//it++;
			if (*it < *b.begin())
			{
				r2.second++;
				a.erase(it);
				it = a.begin();
				auto jt = b.end();
				jt--;
				b.erase(jt);
			}
			else
			{
				r2.first++;
				a.erase(it);
				it = a.begin();
				b.erase(b.begin());
			}
		}

		
		
		
		
		
		out << "Case #" << II << ": " << r2.first<< " " << r1.first << "\n";
		
	}
	
	out.close();
	in.close();
	return 0;
}