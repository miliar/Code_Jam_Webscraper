#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,i,j,k;
	scanf("%d",&t);
	for(k=0;k<t;k++){
		char a[1000];
		scanf("%s",a);
		int l = strlen(a);
		int nplus=0,nminus=0;
		for(i=0;i<l-1;i++){
			if(a[i]=='+')
			{
				if(a[i+1]=='-')
				{
					nplus++;
				}
			}
			if(a[i]=='-')
			{
				if(a[i+1]=='+')
				{
					nminus++;
				}
			}
		}
		if(a[l-1]=='+')
			nplus++;
		else
			nminus++;
		if(a[0]=='+')
		{
			if(a[l-1]=='+')
				printf("Case #%d: %d\n",k+1,nplus*2-2);
			else
				printf("Case #%d: %d\n",k+1,nplus*2);
		}
		else
		{
			printf("Case #%d: %d\n",k+1,nminus*2-1);
		}
	}
}