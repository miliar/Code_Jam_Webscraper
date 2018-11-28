#include <iostream>
#include <fstream>
using namespace std;
short magic1[4][4] = {0}, magic2[4][4] = {0};
int T;
ofstream write;

int main()
{
	write.open("output.txt");
	int a, b, i, j, result, k, m;
	cin >> T;
	for(k = 1; k <= T; k++)
	{
		result = 0;
		cin >> a;
		a--;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				cin >> magic1[i][j];
		cin >> b;
		b--;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				cin >> magic2[i][j];
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				if(magic1[a][i] == magic2[b][j])
				{
					result++;
					m = magic1[a][i];
				}
		if(result == 1)
			write << "Case #" << k << ": " << m << endl;
		else if(result > 1)
			write << "Case #" << k << ": Bad magician!" << endl;
		else
			write << "Case #" << k << ": Volunteer cheated!" << endl;
	}
	system("pause");
	return 0;
}