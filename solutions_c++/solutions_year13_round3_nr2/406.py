#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>
#include<queue>

using namespace std;

void main(){
#ifdef MY_TEST_VAR
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif

   int T;
   scanf("%d", &T);
   for (int I = 1; I <= T; I++)
   {
	   int x,y;
	   scanf("%d%d", &x, &y);
	   printf("Case #%d: ", I);
	   for (int i = 0; i < x; i++)
	   printf("WE");
	   for (int i = x; i < 0; i++)
	   printf("EW");
	   for (int i = 0; i < y; i++)
	   printf("SN");
	   for (int i = y; i < 0; i++)
	   printf("NS");
	   printf("\n");
   }
}