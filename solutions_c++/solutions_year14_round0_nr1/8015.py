#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() 
{
	int T,row1,row2,cont=0, equal;
	vector<vector<int>> M1,M2;
	scanf("%d ", &T);
	for(int i=0;i<T;i++)
	{
		M1.resize(4);
		M1[0].assign(4, 1);
		M1[1].assign(4, 1);
		M1[2].assign(4, 1);
		M1[3].assign(4, 1);
		
		M2.resize(4);
		M2[0].assign(4, 1);
		M2[1].assign(4, 1);
		M2[2].assign(4, 1);
		M2[3].assign(4, 1);
		
		cont=0;
		scanf("%d ", &row1);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				scanf("%d ", &M1[j][k]);
		}
		scanf("%d ", &row2);
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				scanf("%d ", &M2[j][k]);
		}
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				if(M2[row2-1][k]==M1[row1-1][j])
				{
					equal = M2[row2-1][k];
					cont++;
				}
		}
		if(cont==0)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else if(cont==1)
			printf("Case #%d: %d\n",i+1, equal);
		else
			printf("Case #%d: Bad magician!\n",i+1);	
	}
	return 0;
}