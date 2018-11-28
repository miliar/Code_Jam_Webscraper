#include <iostream>
#include <string.h>

int main ()
{
	//freopen("A-large (1).in","r",stdin);
	//freopen("output_file.out","w",stdout);
	int t,i,j,k,ca=0;
	char s[2000],ans[2000];
	scanf("%d",&t);
	//printf("%dhello ",t);
	while(t--)
	{
		ca++;
		for(i=0;i<2000;i++)
		{
			ans[i]='#';
		}
		i=k=1000;
		j=1;
		scanf("%s",&s);
		ans[i]=s[0];
		//printf("%c",ans[i]);
		while(j<strlen(s))
		{
			char t=ans[k];
			if(s[j]>=t)
			{
				ans[k-1]=s[j];
				k--;
				j++;
				t=ans[k];
			}
			else
			{
				ans[i+1]=s[j];
				i++;
				j++;
				//printf("%c",ans[i]);
			}
		}
		printf("Case #%d: ",ca);
		for(i=0;i<2000;i++)
		{
			if(ans[i]!='#')
			{
				printf("%c",ans[i]);
			}
		}
		printf("\n");
		
	}
  return 0;
}                      
 
