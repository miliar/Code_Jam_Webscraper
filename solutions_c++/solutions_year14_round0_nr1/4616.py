#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;
// #define INPUT_FILE

int main(int argc, char const *argv[])
{
	#ifdef INPUT_FILE
	    freopen("A-small-attempt0.in", "r", stdin);
	#endif
	int t;
	scanf("%d", &t);
	int n = t;
	while(t--)
	{
		std::vector<vector<int> > I1(4, vector<int>(4));
		std::vector<vector<int> > I2(4, vector<int>(4));
		int r1, r2;
		scanf("%d", &r1);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &I1[i][j]);
		scanf("%d", &r2);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &I2[i][j]);
		r1--;
		r2--;
		set<int> S;
		for (int i = 0; i < 4; ++i)
		{
			S.insert(I1[r1][i]);
			S.insert(I2[r2][i]);
		}
		if(S.size() == 7)
		{
			for (std::set<int>::iterator i = S.begin(); i != S.end(); ++i)
			{
				if((find(I1[r1].begin(),I1[r1].end(),*i) != I1[r1].end()) && (find(I2[r2].begin(),I2[r2].end(),*i) != I2[r2].end()))
				{
					printf("Case #%d: %d\n", n-t, *i);
					break;
				}
			}
		}
		if(S.size() == 8)
			printf("Case #%d: Volunteer cheated!\n", n-t);
		if(S.size() < 7)
			printf("Case #%d: Bad magician!\n", n-t);
	}
	return 0;
}
