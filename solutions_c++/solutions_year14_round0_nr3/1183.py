#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

typedef vector<pair<int,int> > coord;

int r,c,m;
int rec;
char mine[10][10];

coord refresh(int row, int col) {
	coord temp;
	if((col-1) > 0) {
		if(mine[row][col-1] != '0') {
			mine[row][col-1] = '0';
			temp.push_back(make_pair(row,col-1));
		}
	}
	if((col+1) <= c) {
		if(mine[row][col+1] != '0') {
			mine[row][col+1] = '0';
			temp.push_back(make_pair(row,col+1));
		}
	}
	if((row+1) <= r) {
		if(mine[row+1][col] != '0') {
			mine[row+1][col] = '0';
			temp.push_back(make_pair(row+1, col));
		}
	}
	if((row-1) > 0) {
		if(mine[row-1][col] != '0') {
			mine[row-1][col] = '0';
			temp.push_back(make_pair(row-1, col));
		}
	}
	if((row+1) <= r && (col+1) <= c) {
		if(mine[row+1][col+1] != '0') {
			mine[row+1][col+1] = '0';
			temp.push_back(make_pair(row+1, col+1));
		}
	}
	if((row+1) <= r && (col-1) > 0) {
		if(mine[row+1][col-1] != '0') {
			mine[row+1][col-1] = '0';
			temp.push_back(make_pair(row+1, col-1));
		}
	}
	if((row-1) > 0 && (col+1) <= c) {
		if(mine[row-1][col+1] != '0') {
			mine[row-1][col+1] = '0';
			temp.push_back(make_pair(row-1, col+1));
		}
	}
	if((row-1) > 0 && (col-1) > 0) {
		if(mine[row-1][col-1] != '0') {
			mine[row-1][col-1] = '0';
			temp.push_back(make_pair(row-1, col-1));
		}
	}
	return temp;
}

void clean(coord temp)
{
	for(int i=0;i<temp.size();i++) {
		mine[temp[i].first][temp[i].second] = '.';
	}
}

int isSolve(int row, int col, int count) {
	coord mod;
	mod = refresh(row, col);
	if((count + mod.size()) > rec) {
		clean(mod);
		return 0;
	} else if((count + mod.size()) == rec) {
		return 1;
	}
	int flag = 0;
	for(int i=0;i<mod.size();i++) {
		if(isSolve(mod[i].first, mod[i].second, count+mod.size())) {
			flag = 1;
			break;
		}
	}
	if(!flag) {
		clean(mod);
		return 0;
	} else {
		return 1;
	}
}

void drawMap() {
	for(int i=1;i<=r;i++) {
		for(int j=1;j<=c;j++) {
			if(mine[i][j] == '0') mine[i][j] = '.';
			else mine[i][j] = '*';
		}
	}
	mine[1][1] = 'C';
	for(int i=1;i<=r;i++) {
		for(int j=1;j<=c;j++) {
			printf("%c",mine[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) {
		memset(mine,'.',sizeof(mine));
		scanf("%d%d%d",&r,&c,&m);
		rec = r*c-m;
		mine[1][1] = '0';
		printf("Case #%d:\n",i);
		if((r*c)-m == 1 || (r*c)-m == 0) {
			drawMap();
		}
		else if(isSolve(1,1,1)) {
			drawMap();
		} else {
			printf("Impossible\n");
		}
	}
	return 0;
}
