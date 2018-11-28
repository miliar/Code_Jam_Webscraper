#include<stdio.h>
int main()
{
	int t,n,i,c,sum;
	char str[1005];
	int j = 0;
	FILE *fp1,*fp2;
		fp1 = fopen("A-small-attempt3.in","r");
		fp2 = fopen("out2.o","w");
		fscanf(fp1,"%d",&t);
	while(j!=t){
		fscanf(fp1,"%d %s",&n,str);
		sum = 0;
		c = 0;
		sum = (str[0]-'0');
		//printf("%d\n",sum);
		for(i=1;i<=n;i++){
			 if(sum<i&&(str[i]-'0')!=0){
				c += i-sum;
				sum += c;
				//printf("%d ",c);
			}
			//printf("%d\n",i);
			sum += (str[i]-'0');
		}
		j++;
		fprintf(fp2,"Case #%d: %d\n",j,c);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}
