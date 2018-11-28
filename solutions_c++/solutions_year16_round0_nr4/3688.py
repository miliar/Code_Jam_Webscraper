#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,cont=1;
	scanf("%d",&t);
	while(cont<=t)
	{
		int k,c,s;
		scanf("%d%d%d",&k,&c,&s);
		if(c==1 and s==k) 
		{
			printf("Case #%d: ",cont);
			for(int i=1;i<=k;i++) printf("%d ",i);
			printf("\n");
		}
		else if(c==1 && s<k) printf("Case #%d: IMPOSSIBLE\n",cont); 
		else if(s<k-1) printf("Case #%d: IMPOSSIBLE\n",cont);
		else{
			printf("Case #%d: ",cont);
			for(int i=1+(k>1);i<=k;i++) printf("%d ",i);
			printf("\n");
		}
		cont++;
	}
}