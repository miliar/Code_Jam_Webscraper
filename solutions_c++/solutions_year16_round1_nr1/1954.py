#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	//freopen ("input.txt","r",stdin);
	
	int t,start,end,k,n,i;
	char ans[100000],str[1001];
	
	scanf("%d",&t);
	while(k<=t)
	{
	
		scanf("%s",str);
		//printf("%s\n",str);
	
		start=5000;end=5000;
		n=strlen(str);
		
		ans[start]=str[0];
		
		for(i=1 ; i<n ; i++)
		{
			if(ans[start]>str[i])
			{
				end++;
				ans[end]=str[i];
			}
			else
			{
				start--;
				ans[start]=str[i];
			}
		}
		end++;
		ans[end]='\0';
		//printf("%s\n",&ans[start]);

		 printf("Case #%d: %s\n",k,&ans[start]);
		/*for(i=start ; i<=end ; i++)
		{
			printf("%c",ans[i]);
		}
		printf("\n");*/
		
		k++;

	}
	return 0;
}
