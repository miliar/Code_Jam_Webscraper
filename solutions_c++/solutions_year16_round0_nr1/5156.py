#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,i,j,k;
	scanf("%d",&t);
	for(k=0;k<t;k++){
		int n;
		scanf("%d",&n);
		int a[10]={-1};
		int d = n;
		int flag=0;
		for(i=1;i<=1000;i++){
			flag=0;
			int s = d*i;
			int temp = s;
			while(s!=0)
			{
				a[s%10]=s%10;
				//printf("%d MKK\n",a[s%10]);
				s = s/10;
			}
			for(j=0;j<10;j++)
			{
				if(a[j]!=j)
					flag=1;
				//printf("%d %d\n",j,a[j]);

			}
			if(flag==0){
				printf("Case #%d: %d\n",k+1,temp);
				break;
			}
		}
		if(flag==1)
			printf("Case #%d: INSOMNIA\n",k+1);
	}
}