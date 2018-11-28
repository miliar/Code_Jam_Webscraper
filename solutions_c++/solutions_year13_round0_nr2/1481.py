#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>
#include<queue>

using namespace std;

int field[110][110];

void main(){
#ifdef MY_TEST_VAR
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
   int n;
   scanf("%d", &n);
   for (int I = 1; I <= n; I++)
   {
	   printf("Case #%d: ", I);
	   bool ok = 1;
	   int N, M;
	   scanf("%d%d",&N,&M);
	   for (int i = 0; i < N; i++)
		   for (int j = 0; j < M; j++)
			   scanf("%d", &field[i][j]);

	   for (int i = 0; i < N; i++)
		   for (int j = 0; j < M; j++)
		   {
			   bool b1 = 1, b2 = 1;
			   for (int k = 0; k < N; k++)
				   b1 = b1 && (field[i][j] >= field[k][j]);

			   for (int k = 0; k < M; k++)
				   b2 = b2 && (field[i][j] >= field[i][k]);

			   ok = ok && (b1 || b2);
		   }
	   if (ok)
		   printf("YES\n");
	   else
		   printf("NO\n");
   }
}