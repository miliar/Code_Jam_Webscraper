#include <iostream>

using namespace std;

int main()
{
	int test, fc, sc, cs[16], r;
	int fa[4][4], sa[4][4], c;
	cin >> test;
	for(int i=0; i<test; i++)
	{
		c = 0;
		cin >> fc;
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				cin >> fa[j][k];

		for(int j=0; j<16; j++)
			cs[j] = 0;
		for(int j=0; j<4; j++)
			cs[fa[fc-1][j] - 1] = 1;

		cin >> sc;
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				cin >> sa[j][k];

		for(int j=0; j<4; j++)
		{
			if(cs[sa[sc-1][j] - 1] == 1)
			{
				c++;
				r = sa[sc-1][j];
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(c == 1)
			cout << r;
		else if(c == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
