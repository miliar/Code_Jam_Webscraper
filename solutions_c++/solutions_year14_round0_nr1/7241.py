//by jackyliuxx
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
using namespace std;

int card[5][5];
int cp[20];

int main () {
	int t,k=1;
	scanf("%d",&t);
	while(t--){
		int l;
		scanf("%d",&l);
		int i,j;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&card[i][j]);
				if(i+1==l)
					cp[card[i][j]]=1;
				else
					cp[card[i][j]]=0;
			}
		}
		scanf("%d",&l);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scanf("%d",&card[i][j]);
		int ans=-1;
		for(j=0;j<4;j++){
			if(cp[card[l-1][j]]==1){
				if(ans==-1)
					ans=card[l-1][j];
				else
					ans=9999;
			}
		}
		printf("Case #%d: ",k++);
		if(ans==-1)
			puts("Volunteer cheated!");
		else if(ans==9999)
			puts("Bad magician!");
		else
			printf("%d\n",ans);
	}
}
