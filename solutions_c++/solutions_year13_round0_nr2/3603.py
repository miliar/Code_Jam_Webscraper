#include <iostream>
#include <string>
#include <Cmath>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{
	ofstream output;
	output.open ("output2.in");
	int N, M, T, Min=100, Max=0;
	
	cin >> T;
	
	for (int i=0; i< T; i++)
	{
		int h[100][100]={0};
		bool isBreak = false, beAble=true;
		
		cin >> N >> M;
		
		for (int j=0; j< N; j++)
		{
			for (int k=0; k< M; k++)
			{
				cin >> h[j][k];
				Min = min(h[j][k],Min);
				Max = max(h[j][k],Max);
			}
		}

		for (int j=Min; j<= Max; j++)
		{
			for (int k=0; k<N; k++)
			{
				for (int l=0; l<M; l++)
				{
					bool isRow = true, isCol=true;
					if (h[k][l]==j)
					{
						for (int m=0; m< M; m++)
						{
							if (h[k][m]>j) 
							{
								isRow = false;
								break;
							}
						}
						for (int m=0; m< N; m++)
						{
							if (h[m][l]>j) 
							{
								isCol = false;
								break;
							}
						}
						if (isRow == false && isCol == false) 
						{
							isBreak = true;
							beAble = false;
							break;
						}
					}
					if(isBreak) break;
				}
				if(isBreak) break;
			}
			if(isBreak) break;
		}
		if (beAble) output << "Case #"<<i+1<<": "<<"YES"<< endl;
		else output << "Case #"<<i+1<<": "<<"NO"<< endl;
		
	}
	return 0;
}