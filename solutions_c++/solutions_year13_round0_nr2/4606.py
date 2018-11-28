#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <ctype.h>

using namespace std;

int lin, col;
int maxlin[105], maxcol[105], m[105][105];
int deplin[105], depcol[105], vislin[105], viscol[105];

void cline(int i){
	for(int j=0;j<col;j++){
		if(!viscol[j] && maxcol[j]>m[i][j]){
			depcol[j]--;
		}
	}
}

void ccolune(int j){
	for(int i=0;i<lin;i++){
		if(!vislin[i] && maxlin[i]>m[i][j]){
			deplin[i]--;
		}
	}
}

void lines(){
	for(int i=0;i<lin;i++){
		if(!vislin[i] && !deplin[i]){
			cline(i);
			vislin[i]=1;
		}
	}
}

void colunes(){
	for(int i=0;i<col;i++){
		if(!viscol[i] && !depcol[i]){
			ccolune(i);
			viscol[i]=1;
		}
	}
}

int main(){
	int i, j, t, tes, v, flag;
	scanf(" %d", &t);	
	for(tes=1;tes<=t;tes++){
		memset(maxlin, 0, sizeof(maxlin));
		memset(maxcol, 0, sizeof(maxcol));
		memset(deplin, 0, sizeof(deplin));
		memset(depcol, 0, sizeof(depcol));
		memset(vislin, 0, sizeof(vislin));
		memset(viscol, 0, sizeof(viscol));
		flag=0;
		scanf(" %d %d", &lin, &col);
		for(i=0;i<lin;i++){
			for(j=0;j<col;j++){
				scanf(" %d", &v);
				if(v>maxcol[j])
					maxcol[j]=v;
				if(v>maxlin[i])
					maxlin[i]=v;
				m[i][j]=v;
			}
		}
		for(i=0;i<lin;i++){
			for(j=0;j<col;j++){
				if(m[i][j]<maxlin[i])
					deplin[i]++;
				if(m[i][j]<maxcol[j])
					depcol[j]++;
			}
		}
		for(i=0;i<=min(lin, col);i++){
			lines();
			colunes();
		}
		for(i=0;i<lin && !flag;i++)
			if(deplin[i])
				flag=1;
		for(i=0;i<col && !flag;i++)
			if(depcol[i])
				flag=1;
		printf("Case #%d: ", tes);
		if(flag)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
