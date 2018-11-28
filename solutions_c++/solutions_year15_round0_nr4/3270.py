#include <cstdio>
#include <algorithm>

using namespace std;



int t;
int a[5][5][5];


int main(){
	
	a[2][1][1] = 0;
	a[2][1][2] = 1;
	a[2][1][3] = 0;
	a[2][1][4] = 1;
	a[2][2][2] = 1;
	a[2][2][3] = 1;
	a[2][2][4] = 1;
	a[2][3][3] = 0;
	a[2][3][4] = 1;
	a[2][4][4] = 1;

	
	a[3][1][1] = 0;
	a[3][1][2] = 0;
	a[3][1][3] = 0;
	a[3][1][4] = 0;
	a[3][2][2] = 0;
	a[3][2][3] = 1;
	a[3][2][4] = 0;
	a[3][3][3] = 1;
	a[3][3][4] = 1;
	a[3][4][4] = 0;


	a[4][1][1] = 0;
	a[4][1][2] = 0;
	a[4][1][3] = 0;
	a[4][1][4] = 0;
	a[4][2][2] = 0;
	a[4][2][3] = 0;
	a[4][2][4] = 0;
	a[4][3][3] = 0;
	a[4][3][4] = 1;
	a[4][4][4] = 1;

	scanf("%d", &t);

	int x, r, c;
	for(int q=0; q<t; q++){
		scanf("%d%d%d", &x, &r, &c);
		bool is = false;
		if(x == 1)	is = true;
		is = is || a[x][min(r, c)][max(r, c)];
		if(is)
			printf("Case #%d: GABRIEL\n", q+1);
		else
			printf("Case #%d: RICHARD\n", q+1);
	}

}
