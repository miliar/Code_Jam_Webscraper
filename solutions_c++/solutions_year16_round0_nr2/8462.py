#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;

#define scll(Q)   	scanf("%lld",&Q);
#define sci(Q)   	scanf("%d",&Q);
#define sc(Q)		scanf("%s",&Q);
#define prll(Q)   	printf("%lld\n",Q);
#define pri(Q)    	printf("%d\n",Q);
#define pr(Q)   	printf("%s\n",Q);


int main()
{
	
	int t,i,k,count;
	sci(t);
	for(k=1;k<=t;k++){
		char str[105]={'\0'};
		count=0;
		sc(str);
		if(str[0]=='-')	count++;
				
		for(i=0;i<strlen(str)-1;i++){
			if(str[i]=='+' && str[i+1]=='-')	count+=2;
			
		}
		printf("Case #%d: %d\n",k,count);
	}
	return 0;
}


