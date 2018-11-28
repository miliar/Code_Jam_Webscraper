#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <limits>
#include <cassert>
#include <sstream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;

const int max_n=100010;

int r1,r2;
int a[4][4],b[4][4];
int T;

int main()
{
	scanf("%d",&T);
	for(int z=0; z<T; z++)
	{
		scanf("%d",&r1);r1--;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&a[i][j]);

		scanf("%d",&r2);r2--;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d",&b[i][j]);

		vector<int> R;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(a[r1][i]==b[r2][j])
					R.push_back(a[r1][i]);


		printf("Case #%d: ",z+1);
		int sz=R.size();
		if(sz==0)
			printf("Volunteer cheated!\n");
		else if(sz==1)
			printf("%d\n",R[0]);
		else
			printf("Bad magician!\n");
	}

	return 0;
}