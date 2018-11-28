#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	fstream in("A-large.in", ios::in);
	fstream out("output.txt", ios::out);

	int T;
	in >> T;

	for(int kase = 1 ; kase <= T; ++kase)
	{
		int Smax;
		in >> Smax;
		
		char p[1001];
		for(int i = 0; i < Smax + 1; ++i)
		{
			char tmp;
			in >> tmp;
			p[i] = tmp - '0';
		}

		int nowp = 0;
		int ans = 0;
		for(int i = 0; i < Smax + 1; ++i)
		{
			if(nowp < i)
			{
				ans += (i - nowp);
				nowp += (i - nowp);
			}
			nowp += p[i];
		}
		out << "Case #" << kase << ": " << ans << endl;
	}

	in.close();
	out.close();
	return 0;
}
