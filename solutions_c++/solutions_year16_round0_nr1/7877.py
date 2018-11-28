#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
using namespace std;

int main(){
	long long a,b,c,d,e;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%lld", &a);
	for(int i = 0 ; i < a ; i++){
		int digit[10]={0};
		scanf("%lld", &b);
		if(!b){
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		d=b;
		while(true){
			c=d;
			while(c){
				digit[c%10]=1;
				c/=10;
			}
			bool flag=true;
			for(int j=0;j<10;j++){
				if(!digit[j])
					flag=false;
			}
			if(flag)
				break;
			d+=b;
		}
		printf("Case #%d: %lld\n", i+1, d);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}