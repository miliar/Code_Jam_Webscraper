#include <fstream>
#include <set>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)


int main()
{
	ifstream in("A-small-attempt0 (1).in");
	ofstream out("A.out");
	int t;
	int a[4][4];
	int b[4][4];
	int q, w;
	in >> t;
	for (int II = 1; II <= t; II ++)
	{
		set<int> vv;
		in >> q;
		q--;
		REP(i, 4)
			REP(j, 4)
			in >> a[i][j];
		in >> w;
		w--;
		REP(i, 4)
			REP(j, 4)
			in >> b[i][j];

		
		REP(i,4)
			REP(j,4)
				if (a[q][i] == b[w][j])
					vv.insert(a[q][i]);
		
		out << "Case #" << II << ": ";
		if (vv.size() == 1)
			out << *vv.begin();
		else if (vv.size() == 0)
		{
			out << "Volunteer cheated!";
		}
		if (vv.size() > 1)
		{
			out << "Bad magician!";
		}
		out << "\n";
	}
	out.close();
	in.close();
	return 0;
}