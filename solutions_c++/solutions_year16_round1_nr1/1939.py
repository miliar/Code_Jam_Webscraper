#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");

	int T, t, i;
	string S;

	in >> T;

	t = 1;
	while (t <= T)
	{
		out << "Case #" << t << ": ";

		string ans;

		in >> S;

		ans.insert(0, S, 0, 1);

		i = 1;
		while (i < S.size())
		{
			if (int(S[i]) >= int(ans[0]))
				ans = S[i] + ans;
			else
				ans = ans + S[i];

			i++;
		}

		out << ans << endl;

		t++;
	}

	in.close();
	out.close();

	return 0;
}