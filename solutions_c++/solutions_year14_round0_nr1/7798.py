									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;


int f[4][4],s[4][4];
int main(){
	int tc,i,j,g1,g2;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++)
	{
		scanf("%d",&g1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d",&f[i][j]);

		scanf("%d",&g2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d",&s[i][j]);
		int *a=f[g1-1];
		int *b=s[g2-1];
		sort(a,a+4);
		sort(b,b+4);
		int c=0,r;
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
			{
				if (a[i]==b[j])
					break;
			}
			if (j<4){
				c++;
				r=a[i];
			}
		}
		printf("Case #%d: ",ti);
		if (!c)
			printf("Volunteer cheated!");
		else if (c==1)
			printf("%d",r);
		else
			printf("Bad magician!");
		printf("\n");
	}
	
	
	return 0;
}