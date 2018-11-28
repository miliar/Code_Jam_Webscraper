#include<stdio.h>
int main()
{
	int t,j;
	scanf("%d",&t);
	j=t;
	while(t>0)
	{
		int n;
		char s[100000];
		scanf("%d",&n);
		getchar();
		scanf("%s",s);
		int su=0;
		su+=s[0]-48;
		int no=0;
		int i;
		for( i=1;i<=n;i++)
		{
			// printf("%d %d\n",su,i);
			if(su<i)
			{
				//   printf("bef %d\n",no);
				no+=i-su;
				// printf("after %d\n",no);

				su+=s[i]-48+i-su;
			}
			else
				su+=s[i]-48;
			//printf("sdwre\n");
               }
			t--;
			printf("Case #%d: %d\n",j-t,no);

		}
		return 0;
	}
