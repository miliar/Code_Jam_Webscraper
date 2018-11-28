#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


int main()
{
//            ios_base::sync_with_stdio(0);
		   ifstream plik("A-small-attempt3.in");
		   ofstream wynik("wynik.txt");
			int n,p1,p2;
			int T[2][4];
			vector<int> ans;
			plik>>n;
			string a="Bad magician!\n";
			string b="Volunteer cheated!\n";

			for (int i=1;i<=n;i++)
			{
				plik>>p1;
				for (int j=1;j<=4;j++)
					for (int k=0;k<4;k++)
						if (j==p1)
							plik>>T[0][k];
						else plik>>p2;
				plik>>p2;
				for (int j=1;j<=4;j++)
					for (int k=0;k<4;k++)
						if (j==p2)
							plik>>T[1][k];
						else plik>>p1;
				ans.clear();
				for (int j=0;j<4;j++)
					for (int k=0;k<4;k++)
						if (T[0][j]==T[1][k])
							ans.push_back(T[0][j]);
				wynik<<"Case #"<<i<<": ";
				if (ans.size()==0)
					wynik<<b;
				else if (ans.size()>1)
					wynik<<a;
				else
					wynik<<ans[0]<<endl;
			}
								plik.close();
								wynik.close();

            return 0;
}

