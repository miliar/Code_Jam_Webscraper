#include <iostream>
#include <fstream>

using namespace std;
ifstream in("A-small-attempt0.in-2.txt");
ofstream out("output.txt");


int main(int argc, char *argv[]) {

	int n,m,s,q;
	int a[4][4], b[4][4];
	in >> n;
	for (int T = 0; T < n; ++T)
	{
		in >> m;
		cout << m << endl;
		for (int j = 0; j < 4 ; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				in >> a[j][k];
			}
		}
		in >> s;
		cout << s << endl;
		for (int j = 0; j < 4 ; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				in >> b[j][k];
			}
		}

		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{

				if (a[m -1][i] == b[s-1][j])
				{
					q++;
				}
			}
		}

		if (q == 0)
		{
			//printf("Case #%d: Volunteer cheated!\n", T+1);
			out << "Case #" << T+1 <<": Volunteer cheated!" << "\n";
			q = 0;
		}else if (q == 1)
		{
			for (int i = 0; i < 4; ++i)
			{
				for (int j = 0; j < 4; ++j)
				{

					if (a[m -1][i] == b[s-1][j])
					{
						//printf("Case #%d: %d\n", T+1,a[m -1][i]);
						out << "Case #" << T+1 <<": " << a[m -1][i] << "\n";
						q = 0;
					
					}
				}
			}				
		}else
		{
			//printf("Case #%d: Bad magician!\n", T+1);
			out << "Case #" << T+1 << ": Bad magician!" << "\n";
			q = 0;

		}

	}
}