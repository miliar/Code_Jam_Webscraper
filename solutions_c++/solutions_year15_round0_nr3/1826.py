#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <set>
#include <utility>
#include <stack>

#define rep(i,n) for(int i = 0; i < (n); i++)

using namespace std;

void solve();
void runCase();

char s[10001];
int mat1[4][4] = {
	{0,1,2,3},
	{1,0,3,2},
	{2,3,0,1},
	{3,2,1,0}
};
int mat2[4][4] = {
	{0,0,0,0},
	{0,1,0,1},
	{0,1,1,0},
	{0,0,1,1}
};
int mat3[256];



void runCase()
{
	mat3['1']=0;
	mat3['i']=1;
	mat3['j']=2;
	mat3['k']=3;
	int L,X;
	scanf("%d %d",&L,&X);
	scanf("%s",s);
	int x = 0, y = 0;
	int t = 0, z = 0;
	rep(j,X) 
	rep(i,L) {
		y = (y ^ mat2[x][mat3[s[i]]]);
		x = mat1[x][mat3[s[i]]];
		z = mat1[z][mat3[s[i]]];
		if(t==0) {
			if(x==1) {
				t = 1;
				z = 0;
			}
		} else if(t==1) {
			if(z==2) {
				t = 2;
				z = 0;
			}
		} else if(t==2) {
			if(z==3) {
				t = 3;
				z = 0;
			}
		}
	}
	// cout << x << " " << y << " " << t << endl;
	// int u = x, v = y;
	// rep(i,X-1) {
		// y = (y ^ v ^ mat2[x][u]);
		// x = mat1[x][u];
	// }
	//cout << x << " " << y << endl;
	if(x==0 && y==1 && t==3) printf("YES\n");
	else printf("NO\n");
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	solve();
	return 0;
}
