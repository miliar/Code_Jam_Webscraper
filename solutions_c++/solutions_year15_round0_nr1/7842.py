#include <stdio.h>
#include <stdlib.h>

int main(){
	int t,n,i,j,k,m,x,y,z,a;
	char *s;

	scanf("%d", &t);

	for(k=0;k<t;k++){
		scanf("%d", &n);

		s=(char*)malloc((n+2)*sizeof(char));

		scanf("%s", s);

		x=0,y=n;

		while(x<=y){
			m=(x+y)/2;

			a=m;

			for(i=0;i<n+2;i++)
				if(a>=i)
					a+=(s[i]-'0');
				else
					break;

			if(i==n+2){
				z=m;
				y=m-1;
			}
			else
				x=m+1;
		}

		printf("Case #%d: %d\n", k+1, z);

		free(s);
	}

	return 0;
}