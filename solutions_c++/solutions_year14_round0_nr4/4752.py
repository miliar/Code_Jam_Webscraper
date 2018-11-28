#include <stdio.h>
#include <algorithm>
int main()
{
int t,n;
scanf("%d",&t);
for(n=0;n<t;n++)
	{
	int block,i,j;
	int d_war=0,war=0;
	double bn[1000],bk[1000];
	scanf("%d",&block);
	for(i=0;i<block;i++)
		{
		scanf("%lf",&bn[i]);
		}
	std::sort(bn,bn+block);
	std::reverse(bn,bn+block);
	for(i=0;i<block;i++)
		{
		scanf("%lf",&bk[i]);
		}
	std::sort(bk,bk+block);
	std::reverse(bk,bk+block);

	//war

	for(i=0,j=0;i<block;i++)
		{
		if(bn[i]>bk[j]) {war++;}
		else j++;
		}

	//deceitful war
 std::reverse(bk,bk+block);
 for(i=0,j=block-1;bn[j]<bk[i] && j>-1;j--);
 std::reverse(bk,bk+j+1);
 i=j;
 while(i>-1)
 {
  if(bn[i]>bk[j])
		{d_war++;i--;j--;}
  else
      i--;
}

	/*for(i=0;i<block;i++)
		{
		if(bn[i]>bk[i]){d_war++;}
		else
			{
			std::reverse(bk,bk+block);
			if(bn[i]>bk[i]) {d_war++;}
			}
		}*/

	printf("Case #%d: %d %d\n",n+1,d_war,war);
	}
return 0;
}




