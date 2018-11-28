#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

#define rep(i,n) for(int i = 0; i < (n); i++)

void runCase()
{
	int a1,a2;
	int b1[4][4],b2[4][4];
	
	scanf("%d",&a1);
	rep(i,4) rep(j,4) scanf("%d",&b1[i][j]);
	scanf("%d",&a2);
	rep(i,4) rep(j,4) scanf("%d",&b2[i][j]);
	//printf("%d,",a2);
	
	int x,y;
	x = 0; y = -1;
	rep(ii,16) {
		int k = ii+1;
		int l=0;
		rep(i,4) rep(j,4) if(b1[i][j]==k&&i==a1-1) l++;
		rep(i,4) rep(j,4) if(b2[i][j]==k&&i==a2-1) l++;
		if(l==2) {x++;y = k;}
	}
	
	if(x==1) {
		printf("%d\n",y);
	} else if(x>1) {
		printf("Bad magician!\n");
	} else {
		printf("Volunteer cheated!\n");
	}
	
}

void runSample()
{
	string input;

	char buf[501] = {0};
	cin.getline(buf,501);

	input = buf;


	printf("%s\n",input.c_str());
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
