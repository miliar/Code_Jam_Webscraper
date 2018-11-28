#include <iomanip>
#include <algorithm>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

using namespace std;

int a[20];

void doit()
{
	int x;
	scanf("%d",&x); x--;
	for (int i = 0; i < 4; i++)
	for (int j = 0; j < 4; j++)
	{
		int y;
		scanf("%d",&y);
		if (x == i) { a[y-1]++; }
	}
};

int main()
{
	int T;
	scanf("%d",&T);	
	for (int T_t = 1; T_t <= T; T_t++)
	{
		printf("Case #%d: ",T_t);
		
		for (int i = 0; i < 16; i++) a[i] = 0;
	
		doit();
		doit();

		int j = 0,k = 0;
		for (int i = 0; i < 16; i++)
			if (a[i] == 2) { j++;  k = i; }

		if (j == 0) printf("Volunteer cheated!\n");
		else if (j > 1) printf("Bad magician!\n");
		else printf("%d\n",k+1);
	}

	return 0;	
}
