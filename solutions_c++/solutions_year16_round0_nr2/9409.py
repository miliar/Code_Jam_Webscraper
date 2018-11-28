#include<stdio.h>

int main()
{
	int t,i,j,l,ans,tmp;
	bool s[100],check;
	char ch;
	FILE *fp,*fp1;
	if((fp = fopen("B-large.in","r")) == NULL) {
		printf("Cannot open the file\n");
		return 0;
	}
	fp1 = fopen("b-large-output.in","w");
	fscanf(fp,"%d",&t);
	//scanf("%d",&t);
	ch=getc(fp);
	//ch=getchar();
	for(i = 1;i <= t;i++){
		ans = 0;
		l = 0;
		while(1) {
			ch=getc(fp);
			//ch=getchar();
			if(ch == '\n') break;
			else if(ch =='+') s[l] = true;
			else s[l] = false;
			l++;	
		}
		l--;
		check = true;
		while(l>=0) {
			if(s[l]==check)	{
				l--;
				continue;
			} else  {
				if(check == false) check = true;
				else check = false;
			}
			ans++;
			l--;
		}
		fprintf(fp1,"Case #%d: %d\n",i,ans);
	//	printf("Case #%d: %d\n",i,ans);
	}
	fclose(fp);
	return 0;
}
