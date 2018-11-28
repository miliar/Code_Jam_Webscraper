#include <iostream>
#include <algorithm>
#include <cmath>
#include <assert.h>
#include <stdio.h>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
 
#define INF (1<<30)
#define pii pair<int,int>
#define pll pair<long long,long long>
#define eps 1e-9
 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

using namespace std;

int v[20];
int M[5][5];

main(){

		int te;
		scanf("%d",&te);

		for(int t=1;t<=te;t++){

			memset(v,0,sizeof(v));

			int a,b;
			scanf("%d",&a);

			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					scanf("%d",&M[i][j]);

			for(int i=0;i<4;i++)
				v[M[a-1][i]]++;

			scanf("%d",&b);

			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					scanf("%d",&M[i][j]);

			for(int i=0;i<4;i++)
				v[M[b-1][i]]++;

			int qnt = 0;
			int ans = 0;

			for(int i=1;i<=16;i++)
				if(v[i] == 2)
					qnt++,
					ans = i;

			printf("Case #%d: ",t);

			if(qnt == 1)
				printf("%d\n",ans);
			if(qnt == 0)
				printf("Volunteer cheated!\n");
			if(qnt > 1)
				printf("Bad magician!\n");

			}


		}
