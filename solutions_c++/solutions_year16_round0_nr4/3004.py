#include<iostream>
using namespace std;
int main()
{
	int t,K,C,S,i,p=0;
	freopen("4th.in","r",stdin);
		freopen("output4th.txt","w",stdout);
  scanf("%d",&t);
  while(t--)
  {
  	p++;
  	scanf("%d",&K);
  	scanf("%d",&C);
  	scanf("%d",&S);
  	printf("Case #%d: ",p);
  	for(i=1;i<=K;i++)
  	{
  		printf("%d ",i);
	  }
	  printf("\n");
  }
		fclose(stdin);
	fclose(stdout);
	
	return 0;
}
