#include<cstdio>

using namespace std;


int main()
{

	int t1,t,x1,r1,c1;;

	freopen("output.txt", "w" , stdout);
	freopen("input.txt", "r" ,stdin);

	scanf("%d",&t1);
	for (t=1;t<=t1;t++)
	{
    	
    	scanf("%d %d %d",&x1,&r1,&c1);
    	if (x1==1)
    	printf("Case #%d: GABRIEL\n",t);
    	else if (x1==2 && r1*c1%x1==0)
    	printf("Case #%d: GABRIEL\n",t);
    	else if (x1==2 && r1*c1%x1!=0)
    	printf("Case #%d: RICHARD\n",t);
    	else if (x1==3 && ((r1==2 && c1==3) || (r1==3 && c1==2) ||(r1==4 && c1==3) ||(r1==3 && c1==4) ||(r1==3 && c1==3)))
    	printf("Case #%d: GABRIEL\n",t);
    	else if (x1==3)
    	printf("Case #%d: RICHARD\n",t);
    	else if (x1==4 && ((r1==4 && c1==3) || (r1==3 && c1==4) ||(r1==4 && c1==4)))
    	printf("Case #%d: GABRIEL\n",t);
    	else if (x1==4)
    	printf("Case #%d: RICHARD\n",t);
	}
    return 0;
}
