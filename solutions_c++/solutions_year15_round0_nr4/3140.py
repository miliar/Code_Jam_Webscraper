#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		int flag=0;
		if(a==1)
			flag=1;
		else if(a==2&&(((b*c)%2==0)))
			flag=1;
		else if(a==3&&((b==2&&c==3)||(b==3&&c==2)||(b==3&&c==4)||(b==4&&c==3)||(b==3&&c==3)))
			flag=1;
		else if(a==4&&((b==4&&c==4)||(b==3&&c==4)||(b==4&&c==3))) flag=1;

		if(flag==1)
			printf("GABRIEL\n");
		else printf("RICHARD\n");
	}
	return 0;
}
