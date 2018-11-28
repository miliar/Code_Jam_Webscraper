#include <iostream>
#include <cstdio>
using namespace std;

int r,c;
int t[105][105];
int sum[105][105];

int getSum(int x, int y, int a, int b) {
	return sum[a][b]-sum[x-1][b]-sum[a][y-1]+sum[x-1][y-1];
}

int ans() {
	for (int i = 0; i<=max(r, c); i++) { sum[0][i] = 0; sum[i][0] = 0; t[i][0] = 0; t[0][i] = 0; }
	for (int i = 1; i<=r; i++) {
    	for (int j = 1; j<=c; j++) {
    		sum[i][j] = sum[i][j-1]+sum[i-1][j]-sum[i-1][j-1];
    		if (t[i][j]>0) sum[i][j]++;
    	}
    }
    
    //cout << getSum(1, 1, 2, 1);
    int re = 0;
    
    for (int i = 1; i<=r; i++) for (int j = 1; j<=c; j++) {
    	if (t[i][j] == 0) continue;
    	int sec = getSum(i, 1, i, j)+getSum(1, j, i, j)+getSum(i, j, i, c)+getSum(i, j, r, j)-4;
    	if (sec == 0) return -1;    	
    	if (t[i][j] == 1) {
    		if (getSum(i, 1, i, j)-1 == 0) re++;
    		continue;
    	}
    	if (t[i][j] == 2) {
    		if (getSum(i, j, i, c)-1 == 0) re++;
    		continue;
    	}
    	if (t[i][j] == 3) {
    		if (getSum(1, j, i, j)-1 == 0) re++;
    		continue;
    	}
    	if (t[i][j] == 4) {
    		if (getSum(i, j, r, j)-1 == 0) re++;
    		continue;
    	}
    }
    
	return re;
}

int main()
{
    int db; scanf("%d", &db);
    for (int ii = 1; ii<=db; ii++) {
    	scanf("%d %d\n", &r, &c);
    	char c0;
    	for (int i = 1; i<=r; i++) {
    		for (int j = 1; j<=c; j++) {
    			scanf("%c", &c0);
    			if (c0 == '.') t[i][j] = 0;
    			if (c0 == '<') t[i][j] = 1;
    			if (c0 == '>') t[i][j] = 2;
    			if (c0 == '^') t[i][j] = 3;
    			if (c0 == 'v') t[i][j] = 4;
    		}
    		scanf("%c", &c0);
    	}
    	int response = ans();
    	if (response >= 0) printf("Case #%d: %d\n", ii, response);
    	else printf("Case #%d: IMPOSSIBLE\n", ii);
    }
    return 0;
}
