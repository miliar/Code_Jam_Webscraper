#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int k = 1; k <= T; k++)
	{
		int sk;
		in >> sk;
		vector<int> v(sk + 1);
		for (int i = 0; i <= sk; i++)
		{
			char c;
			in >> c;
			v[i] = c - '0';
		}
		int stand = 0;
		int need = 0;
		for (int i = 0; i <= sk; i++)
		{
			if (stand >= i)
			{
				stand += v[i];
			}
			else
			{
				need += (i - stand);
				stand = i;
				stand += v[i];
			}
		}
		out << "Case #" << k << ": " << need << endl;
		cout << "Case #" << k << ": " << need << endl;

	}


	out.close();
	in.close();
}