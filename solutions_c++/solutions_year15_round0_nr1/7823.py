#include<stdio.h>
int main(){
freopen("inputfilename.in","r",stdin);
freopen("outputfilename.in","w",stdout);

	long int i,j,ans,count,a[1001],t,max,number;
	char s[1001];
	scanf("%ld",&t);
	for(j=1;j<=t;j++){
		count=0;
		ans=0;
		scanf("%ld",&max);
		scanf("%s",s);
		for(i=0;i<=max;i++)
		{
			number=s[i]-'0';
			if(count>=i)
			{
				count+=number;
			}
			else {
				count+=number;
				count++;
				ans++;
			}
		}
		printf("Case #%ld:",j);
		printf(" %ld\n",ans);
	}
}
