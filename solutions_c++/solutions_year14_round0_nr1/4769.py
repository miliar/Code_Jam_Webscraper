#include <iostream>
using namespace std;
int main()
{
	int n;
	int ha[5][5];
	int hb[5][5];
	cin >> n;
	for(int c=1; c<=n; ++c)
	{
		int select1,select2;
		cin >> select1;
		for(int i=1; i<=4; ++i)
			for(int j=1; j<=4; ++j)
			{
				cin >> ha[i][j];
			}
		cin >> select2;
		for(int i=1; i<=4; ++i)
			for(int j=1; j<=4; ++j)
			{
				cin >> hb[i][j];
			}
		int count = 0; 
		int value = -1;
		for(int v=1; v<=4; ++v)
			for(int k=1; k<=4; ++k)
			{
				if(ha[select1][v]==hb[select2][k])
				{
					count++;
					value = ha[select1][v];
				}
			}
		if(count == 0)
			cout << "Case #" << c << ": " << "Volunteer cheated!" << endl;
		else if(count == 1)
			cout << "Case #" << c << ": " << value << endl;
		else 
			cout << "Case #" << c << ": " << "Bad magician!" << endl;	
	}
	return 0;
}
