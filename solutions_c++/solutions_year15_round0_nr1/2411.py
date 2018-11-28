#include <stdio.h>
#include<conio.h>


int main() {
	freopen("A-large.in","r",stdin);
	freopen("code.out","w",stdout);
	unsigned long long i,T,s,l,n,k;
	char m[1001];
	scanf("%llu",&T);k=0;
	while(T!=0) {T--;k++;

scanf("%llu %s",&s,m);
i=1;l=0;n=(unsigned long long)m[0]-48;
while(m[i]!='\0'){
	if(n<i){
		l++;n+=(i-n);
	}n+=(unsigned long long)m[i]-48;
	
	
	
	i++;
}
		printf("Case #%d: ", k);
printf("%llu\n",l);

		
		printf("\n");
	}
	return 0;
}
