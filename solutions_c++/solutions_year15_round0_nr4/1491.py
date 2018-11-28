#include <bits/stdc++.h>
using namespace std;
int X,R,C;
 
int main()
 { freopen("que.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nCase;
	scanf("%d", &nCase);
	for (int cs = 1; cs <= nCase; cs++)
	 {
		scanf("%d %d %d", &X,&R,&C);
		int mty = R*C;
		if(X == 1)
		{
			printf("Case #%d: GABRIEL\n", cs);
		}else if(X == 2)
		{
			if(mty%2 == 0){
				printf("Case #%d: GABRIEL\n", cs);
			}else{
				printf("Case #%d: RICHARD\n", cs);
			}
		}
		else if(X == 3)
		{
			if(mty == 6 || mty == 9 || mty == 12)
			{
				printf("Case #%d: GABRIEL\n", cs);
			}
			else
			{
				printf("Case #%d: RICHARD\n", cs);
			}
		}
		else
		{
			if(mty == 12 || mty == 16)
			{
				printf("Case #%d: GABRIEL\n", cs);
			}
			else
			{
				printf("Case #%d: RICHARD\n", cs);
			}
		}
	}
	fclose(stdout);
	return 0;
}
