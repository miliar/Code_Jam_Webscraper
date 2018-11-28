#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;
typedef long long ll;
int xx, yy;
bool tem[100][100];
int maior[100];
double prob;

void calc(int x, int y, double p, int tot){
	if(tot == 0) return;
	tot--;
	if(tem[x-1][y+1] && tem[x+1][y+1]){
		tem[x][y+2] = true;
		maior[x]++;
		if(x == xx && y == yy) prob += p;
		calc(50,(maior[50]-1)*2,p,tot);
		maior[x]--;
		tem[x][y+2] = false;
		return;
	}
	int x1=x,x2=x,yy1=y,yy2=y;
	if(tem[x-1][y+1]){
		while(yy1 >= -1){
			x1++;
			yy1--;
			if(yy1 >= -1 && tem[x1+1][yy1+1]) break;	
		}
		tem[x1][yy1+2] = true;
		maior[x1]++;
		if(x1 == xx && yy1 == yy) prob += p;
		calc(50,(maior[50]-1)*2,p,tot);
		maior[x1]--;
		tem[x1][yy1+2] = false;
		return;
	}
	if(tem[x+1][y+1]){
		while(yy2 >= -1){
			x2--;
			yy2--;
			if(yy2 >= -1 && tem[x2-1][yy2+1]) break;	
		}
		tem[x2][yy2+2] = true;
		maior[x2]++;
		if(x2 == xx && yy2 == yy) prob += p;
		calc(50,(maior[50]-1)*2,p,tot);
		maior[x2]--;
		tem[x2][yy2+2] = false;
		return;
	}
	p /= 2;
		while(yy1 >= -1){
			x1++;
			yy1--;
			if(yy1 >= -1 && tem[x1+1][yy1+1]){
				 break;
			}
		}
		tem[x1][yy1+2] = true;
		maior[x1]++;
		if(x1 == xx && yy1 == yy) prob += p;
		calc(50,(maior[50]-1)*2,p,tot);
		maior[x1]--;
		tem[x1][yy1+2] = false;
	
		while(yy2 >= -1){
			x2--;
			yy2--;
			if(yy2 >= -1 && tem[x2-1][yy2+1]) break;	
		}
		tem[x2][yy2+2] = true;
		maior[x2]++;
		if(x2 == xx && yy2 == yy) prob += p;
		calc(50,(maior[50]-1)*2,p,tot);
		maior[x2]--;
		tem[x2][yy2+2] = false;
		//printf("nao tinha de nenhum lado, parou em %d %d e %d %d\n", x1,yy1,x2,yy2);
}

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int n,t,x,y;
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		printf("Case #%d: ", _);
		scanf("%d %d %d", &n, &x, &y);
		n--;
		tem[50][0] = true;
		memset(maior, 0, sizeof maior);
		maior[50]=1;
		if(x == y && x == 0) printf("1.0000000\n");
		else{
			x += 50;
			xx = x; yy = y-2;
			prob = 0;
			calc(50,0,1.0,n);
			printf("%.7lf\n", prob);
		}
		
	}
	return 0;
}
