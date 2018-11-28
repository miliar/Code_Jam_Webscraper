#include <stdio.h>
#include <algorithm>
using namespace std;

void resolve (int x, int r, int c, bool *gabriel)
{
	if ((r*c)%x!=0)
	{
		*gabriel = false;
		return;
	}
	if (r == 2 && c ==2)
	{
		*gabriel = false;
		return;
	}

	int menor = min(r,c);
	if (menor == 1||menor == 2)
	{
		*gabriel = false;
		return;

	}
	*gabriel = true;
	return;


}
int main()
{
	int t;
	int teste = 0;
	scanf("%d",&t);
	while(t--)
	{

		int x,r,c;
		bool gabriel = false;
		scanf("%d%d%d",&x,&r,&c);
		teste++;
		printf("Case #%d: ",teste);
		 if (x==1||x==2)
		 {
		 	if ((r*c)%x == 0)
		 		gabriel = true;
		 	else 
		 		gabriel = false;
		 }
		 else if (x == 3)
		 {
		 	if ((r*c)%x !=0)
		 		gabriel = false;
		 	else
		 	{
		 		if (r==1||c==1)
		 			gabriel = false;
		 		else gabriel = true;
		 	}
		 }
		 else if (x == 4)
		 {
		 	resolve(x,r,c,&gabriel);
		 }

		 if (gabriel)
		 	printf("GABRIEL\n");
		 else printf("RICHARD\n");
	}
	return 0;
}