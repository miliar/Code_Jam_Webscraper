#include <fstream>
#include <set>

using namespace std;

ifstream in("A-small-attempt0.in");
ofstream out("output.txt");

int main()
{
	int t;
	in >> t;
	for (int i = 0; i < t; i++)
	{
		int f, s;
		set <int> ff, ss, ans;

		in >> f;
		for (int j = 0; j < 4; j++)
		{
			for (int e = 0; e < 4; e++)
			{
				int x;
				in >> x;
				if (j == f - 1)
					ff.insert(x);
			}
		}

		in >> s;
		for (int j = 0; j < 4; j++)
		{
			for (int e = 0; e < 4; e++)
			{
				int x;
				in >> x;
				if (j == s - 1)
					ss.insert(x);
			}
		}

		for (set <int>::iterator it = ff.begin(); it != ff.end(); it++)
		{
			if (ss.find(*it) != ss.end())
				ans.insert(*it);
		}

		out << "Case #" << i + 1 << ": ";

		if (ans.size() == 0)
			out << "Volunteer cheated!" << endl;
		else if (ans.size() > 1)
			out << "Bad magician!" << endl;
		else
			out << *ans.begin() << endl;
	}

	in.close();
	out.close();
	return 0;
}