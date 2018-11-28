#include<stdio.h>
#include<string.h>

int main()
{
	char s[100];
	int t,cnt,l,i,j,k;
	//fscanf("%d",&t);
	FILE *f1,*f2;
	f1=fopen("apr16_1smallout2.txt","w+");
	f2=fopen("B-large.txt","r");
	fscanf(f2,"%d",&t);
	j=1;
	while(t--)
	{
		fscanf(f2,"%s",s);
		cnt=0;
		l=strlen(s);
		cnt=(s[l-1]=='-')?1:0;
		for(i=l-1;i>0;i--) {
			if(s[i]=='-')
			 cnt+=(s[i-1]=='-')?0:1;
			else 
			 cnt+=(s[i-1]=='-')?1:0;
		}
		printf("Case #%d : %d\n",j,cnt);
		fprintf(f1,"Case #%d: %d\n",j,cnt);
		j++;
	}
	fclose(f1);
	fclose(f2);
	return 0;
}
