#include<cstdio>
int main()
{
	int t;
	scanf("%d",&t);
	int ti=0;
	while(ti!=t){
		int smax,sum=0,r=0;
		scanf("%d",&smax);
		char str[smax+1];
		scanf("%s",&str);
		for(int i=0;i<smax+1;i++)
		{
			int temp=str[i]-'0';
			if(temp!=0)
			{
				if(sum>=i)
					sum+=temp;
				else{
					r+=i-sum;
					sum+=r+temp;
				}
			}
		}
		printf("Case #%d: %d\n",ti+1,r);
		ti++;
	}
	return 0;
}
