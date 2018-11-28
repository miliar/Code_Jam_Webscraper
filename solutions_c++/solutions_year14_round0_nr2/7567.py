#include <cstdio>
#include <algorithm>
using namespace std;

int T, t;
double C, F, X, cookie=2;
double sec[1111111]={0,};

void input()
{
	scanf("%lf %lf %lf", &C, &F, &X);
}

void make()
{
	memset(sec, 0, 1111111);
	cookie=2;
	int x=0;
	double postC=0;
	double postX=0;
	double preC=C/cookie;
	double preX=X/cookie;
	sec[x]=preC;
	while(1) {
		cookie+=F;
		postC=C/cookie;
		postX=X/cookie;
		x++;
		sec[x]+=(sec[x-1]+postC);
		if (sec[x-1]+preX-preC < sec[x]+postX-postC)
			break;
		else {
			preC=postC;
			preX=postX;
		}
	}
	printf("Case #%d: %.10lf\n", t,sec[x-1]+preX-preC);

	return;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		input();
		make();
	}
	return 0;
}