#include <iostream>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream at;
	at.open ("at.txt");
	ofstream it;
	it.open ("it.txt");
	
	int t;
	at>>t;

	int a[4][4];
	int s[4][4];

	for (int l=0;l<t;l++)
	{
		int g1;
		at >> g1;
		g1--;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				at >> a[i][j];
			}
		}

		int g2;
		at >> g2;
		g2--;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				at >> s[i][j];
			}
		}
		bool mark=false;
		bool err=false;
		bool wiz = false;
		int r;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				if (mark==true)
				{
					if(a[g1][i]==s[g2][j])
					{
						wiz=true;
					}
				}
				else
				{
					if(a[g1][i]==s[g2][j])
					{
						mark=true;
						r=a[g1][i];
					}
				}
		/*		2
				1 2 3 4
				5 6 7 8
				9 10 11 12
				13 14 15 16
				3
				1 2 5 4
				3 11 6 15
				9 10 7 12
				13 14 8 16 */
			}
		}
		if(!mark)
			it << "Case #"<< l+1 <<": Volunteer cheated!" << endl;
		else if(wiz)
			it << "Case #"<< l+1 <<": Bad magician!" << endl;
		else
			it << "Case #"<< l+1 <<": "<< r << endl;
	}
	return 0;
}
