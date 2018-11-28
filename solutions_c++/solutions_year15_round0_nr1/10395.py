#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

char s[1005];
int rep;
int n;
int stand;
int needadd;
int total;
int main(){
scanf("%d",&rep);

for(int i=1;i<=rep;i++){
	scanf("%d %s",&n,s);
	stand=0;
	needadd=0;
	total =0;
	
	for(int j=0;j<=n;j++){
		if(j<=stand)
		  stand+=(s[j]-'0');
		else {
		  needadd=j-stand;
		  total+=needadd;
		  stand+=needadd;
		  stand+=s[j]-'0';
		}
	}
	
	printf("Case #%d: %d\n",i,total);
}


return 0;
}

