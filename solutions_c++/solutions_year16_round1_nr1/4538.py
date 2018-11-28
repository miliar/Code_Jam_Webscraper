#include<stdio.h>
#include<string.h>
char result[2000];
char lwin[1000];
 void solve(char *s);
int main()
{
	freopen("A-small-attempt1 (1).in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int N,i=1;
	scanf("%d",&N);
	while(N--)
	{
		if(i!=1)	printf("\n");
		char s[1000];
		scanf("%s",s);
		solve(s);
		printf("Case #%d: %s",i,lwin);
		i++;
	}
 } 
 
 void solve(char *s)
 {
 	int i,len = strlen(s);
 	int front=1000,back=1000;
 	memset(result,0,sizeof(result));
 	result[1000] = s[0];
 	
 	for(i=1;i<len;i++)
 	{
 		if(s[i]>=result[front])
 			result[--front]=s[i];
 		else result[++back] = s[i];
	 }
	result[++back]='\0';
	strcpy(lwin,&result[front]);
 }
