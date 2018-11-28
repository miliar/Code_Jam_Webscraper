#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output_3.txt","w",stdout);
	int t,cnt=1;
	scanf("%d",&t);
	while(t--) {
		int x,r,c;
		cin >> x >> r >> c;
		printf("Case #%d: ",cnt++);
		if(x == 1)
		{
			printf("GABRIEL\n");
		}else if(x == 2)
		{
			if((r*c) & 1 ) printf("RICHARD\n");
			else puts("GABRIEL");
		}else if(x == 3)
		{
			if((r == 3 || c == 3) && (r*c) != 3)printf("GABRIEL\n");
			else printf("RICHARD\n");
		}else{
			if((r == 3 && c == 4) || (r == 4 && c ==3) || (r == 4 && c == 4)) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
	}
}
