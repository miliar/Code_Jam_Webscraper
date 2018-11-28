#include<string>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<algorithm>
#include<iomanip>

using namespace std;

#define maxn 4+10
#define oo 1000000000

typedef long long LL;

int ans1, ans2;
int A[maxn][maxn], B[maxn][maxn], tmp[maxn];

void Input() {
	scanf("%d",&ans1);
	for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			scanf("%d",&A[i][j]);
	scanf("%d",&ans2);
	for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			scanf("%d",&B[i][j]);
}

void Solve(int Test) {
	printf("Case #%d: ",Test);
	for (int i = 1; i <= 4; i++)
		tmp[i] = A[ans1][i];
	int t = 0, ok = true;
	for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			if (tmp[i] == B[ans2][j])
				if (t == 0)
					t = tmp[i];
				else ok = false;
	if (!ok)
		 printf("Bad magician!\n");
	else if (t == 0)
		printf("Volunteer cheated!\n");
	else printf("%d\n",t);
}

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; i++) {
	    Input();
	    Solve(i);
	}
    return 0;
}

