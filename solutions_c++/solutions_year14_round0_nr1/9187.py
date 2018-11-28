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
#include <fstream>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;


int main()
{
	int t;
	S(t);
	FORE(i,t)
	{
		int row1,row2,mat1[4][4],mat2[4][4],sol=1;
		S(row1);
		FOR(j,4)
			FOR(k,4)
				S(mat1[j][k]);
		S(row2);
		FOR(j,4)
			FOR(k,4)
				S(mat2[j][k]);
		row1--;
		row2--;
		FOR(k,4)
			if(mat1[row1][k]==mat2[row2][0] || mat1[row1][k]==mat2[row2][1] || mat1[row1][k]==mat2[row2][2] ||mat1[row1][k]==mat2[row2][3])
			{
				sol = 2;
				break;	
			}

		if(sol == 1)
		{
			printf("Case #%d: Volunteer cheated!\n",i);
			continue;
		}

		int cnt = 0;
		int ans = 0;
		for(int m=0;m<4;m++)
		{
			if(mat2[row2][0]==mat1[row1][m])
			{
				cnt++;
				ans=mat2[row2][0];
			}
			if(mat2[row2][1]==mat1[row1][m])
			{
				cnt++;
				ans=mat2[row2][1];
			}
			if(mat2[row2][2]==mat1[row1][m])
			{
				cnt++;
				ans=mat2[row2][2];
			}
			if(mat2[row2][3]==mat1[row1][m])
			{
				cnt++;
				ans=mat2[row2][3];
			}
		}
		if(cnt>1)
			printf("Case #%d: Bad magician!\n",i);
		else
			printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
