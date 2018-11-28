#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <sstream>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

int matrix[7][7];
int matrox[7][7];

int main(){
	freopen("input.txt","r",stdin);
	freopen("o.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int match=0;
	for (int i=1;i<=t;++i){
		int cont=0;
		int g1,g2;
		scanf("%d",&g1);
		for (int f=1;f<=4;++f)
		for (int j=1;j<=4;++j)
		cin>>matrix[f][j];
		
		scanf("%d",&g2);
		
		for (int f=1;f<=4;++f)
		for (int j=1;j<=4;++j)
		cin>>matrox[f][j];

		for (int j=1;j<=4;++j){
			for (int k=1;k<=4;++k){
				if (matrix[g1][j]==matrox[g2][k]){
				cont++;
				match=matrix[g1][j];
				}
			}
		}

		printf("Case #%d: ",i);
		if (cont==1)
		printf("%d\n",match);
		else if (cont==0)
		printf("Volunteer cheated!\n");
		else
		printf("Bad magician!\n");
	}


return 0;
}
