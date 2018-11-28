#include<stdio.h>
#include<string.h>
int main(){
	int tc,i,l,num=1,j;
	scanf("%d",&tc);
	while(tc--){
		char str[1009],temp;
		scanf("%s",str);
		l=strlen(str);
		for(i=1 ; i<l ; i++)
		{
				if(str[i]>=str[0])
				{
					
					temp=str[i];
					for(j=i ; j>=0 ; j--)
					str[j]=str[j-1];
					str[0]=temp;
				}
		}
		printf("Case #%d: %s\n",num++,str);
	}
	return 0;
}
