#include <iostream> 
#include <cstdio>
using namespace std;


int main() 
{ 
    freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 0; t < T; ++t) 
	{	
		printf("Case #%d: ", t + 1);
		int gA[4][4];
		int gB[4][4];
		int ansA, ansB;
		int count = 0;
		int key;

		cin >> ansA;
		for(int i=0; i < 4; i++)
			for(int j=0; j < 4; j++)
				cin >> gA[i][j];

		/*cout << ansA;
		for(int i=0; i < 4; i++)
		{
			for(int j=0; j < 4; j++)
			{
				cout << gA[i][j] << " ";
			}
			cout << endl;
		}*/
		
		cin >> ansB;
		for(int i=0; i < 4; i++)
			for(int j=0; j < 4; j++)
				cin >> gB[i][j];
		//###############################################################
		//###############################################################

		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(gA[ansA - 1][i] == gB[ansB - 1][j])
				{
					++count;
					if(count == 1)
						key = gA[ansA - 1][i];
				}
			}
		}

		if(count == 0)
			cout << "Volunteer cheated!";
		else if(count == 1)
			cout << key;
		else if(count >= 2)
			cout << "Bad magician!";
		
		
		printf("\n");
	}
		//system("pause");
		return 0;

}

