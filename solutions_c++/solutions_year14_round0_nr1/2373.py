#include <iostream>
using namespace std;

void main()
{
#ifdef LATTE
	freopen("A-small-attempt0.in","r",stdin);  
	freopen("out.out", "w", stdout);
#endif // LATTE

	int t, caset = 0;
	cin >> t;
	while (t--)
	{
		int carda[4][4],cardb[4][4];
		int linea, lineb;
		cin >> linea;
		linea--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> carda[i][j];
			}
		}
		cin >> lineb;
		lineb--;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> cardb[i][j];
			}
		}
		int found[4] = { 0 };
		int k = -1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (carda[linea][i] == cardb[lineb][j])
				{
					k++;
					found[k] = carda[linea][i];
					
				}
			}
		}
		caset++;
		if (k==0)
		{
			cout << "Case #" << caset << ": " << found[0] << endl;
		}
		else if (k>0)
		{
			cout << "Case #" << caset << ": Bad magician!" << endl;

		}
		else if (k==-1)
		{
			cout << "Case #" << caset << ": Volunteer cheated!" << endl;
		}

	}
}