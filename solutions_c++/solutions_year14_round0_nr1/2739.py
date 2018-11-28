#include <fstream>

using namespace std;

int tab[4];

int main()
{
	ifstream cin("A-small-attempt1.in",ios::in);
	ofstream cout("A-small-attempt0.out",ios::out);
	int T;
	cin >> T;
	for(int i = 1 ; i<=T;i++)
	{
		int r1, r2;
		cin >> r1;
		for(int j = 1; j<=4;j++)
		{
			for(int k = 0 ; k<4;k++)
			{
				int temp;
				cin >> temp;
				if(j == r1)
					tab[k] = temp;
			}
		}
		cin >> r2;
		int ans = 0;
		bool flag = false;
		for(int j = 1 ; j<=4;j++)
		{
			for(int k = 0 ; k<4;k++)
			{
				int temp;
				cin >> temp;
				if(j == r2)
				{
					for(int o = 0; o<4;o++)
					{
						if(temp == tab[o] && flag == false)
						{
							if(ans != 0)
							{	
								cout << "Case #" << i << ": Bad magician!" << endl;
								flag = true;
								break;
							}
							else
								ans = temp;
							
						}
					}
				}
			}
			
		}
		if(flag == false)
		{
			if(ans != 0)
				cout << "Case #" << i << ": " << ans << endl;
			else
				cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
	}
	cout.close();
	cin.close();
	return 0;
}