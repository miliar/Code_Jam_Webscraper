#include<cstdio>
#include<cmath>
#include<string>
#include<iostream>
using namespace std;
int main(void){
	int t, cs;
	int r, c, x, sx;
	scanf("%d",&t);
	string winner = "";
	cs = 1;
	while(t--){
		scanf("%d %d %d",&x, &r, &c);

		sx = (x+2)/2;
		if((x-sx+1)==1)
			sx=1;
		if( ((r*c)%x!=0) || (x>r && x>c) || sx>r || sx>c )
			winner = "RICHARD";
		else
			winner = "GABRIEL";
		printf("Case #%d: ", cs);
		cout << winner <<"\n";
		cs++;

	}
}