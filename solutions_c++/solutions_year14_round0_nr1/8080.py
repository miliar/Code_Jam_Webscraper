#include<iostream>
#include<vector>
#include<map>
#include<list>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<string>
#include<cmath>
#include<cstdlib>
#include<string.h>
using namespace std;

#define scan(x) scanf("%d",&x)
#define scan2(x,y)	scanf("%d%d",&x,&y)
#define print(x)	printf("%d\n",x)
#define print2(x,y)	printf("%d %d",x,y)

typedef long double ld;
typedef long long ll;

int main(){
	int tmp,row,a[4][4],cnt,t,i,j,l=1;
	scan(t);
	while(t--){
		printf("Case #%d: ",l++);
		int vis[17]={0};
		scan(row);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scan(a[i][j]);
		row--;
		for(i=0;i<4;i++)
			vis[a[row][i]]+=1;
		scan(row);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				scan(a[i][j]);
		row--;
		for(i=0;i<4;i++)
			vis[a[row][i]]+=1;
		cnt=0;
		for(i=1;i<17;i++)
			if(*(vis+i))	cnt++;
		if(cnt==8)
			puts("Volunteer cheated!");
		else if(cnt==7){
			for(i=1;i<17;i++)
				if(*(vis+i)==2){
					print(i);
					break;
				}
		}
		else
			puts("Bad magician!");
	}
	return 0;
}
