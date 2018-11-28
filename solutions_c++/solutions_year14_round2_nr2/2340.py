#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int n;
int a, b, k;

int min(int a, int b){return a>b?b:a;}
int tmin(int a, int b, int c){return min(min(a,b),c);}

int getl(int a){
	int count = 1;
	while(a/2){
		a /= 2;
		count++;
	}
	return count;
}

int main(){
	int t, i, j, count, p, q;
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("test.txt", "w", stdout);
	scanf("%d", &t);
	for(i=0; i<t; i++){
		count = 0;
		scanf("%d %d %d",&a, &b, &k);
		if(a > b){
			a = a^b;
			b = a^b;
			a = a^b;
		}
		int tp = tmin(a,b,k);
		
		count += tp*b + tp*a - tp*tp;
		int l, t;
		for(j=tp; j<a; j++){
			for(p=tp; p<b; p++){
				t = 0;
				if(j > p)l = getl(p);
				else l = getl(j);
				for(q=0; q<l; q++){
					if((j>>q&1) && (p>>q&1))t += 1<<q;
				}
				if(t < k)count++;
			}
		}
		printf("Case #%d: %d\n",i+1,count);		
	}	
	return 0;
}
