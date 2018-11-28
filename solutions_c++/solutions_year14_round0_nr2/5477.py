#include <bits/stdc++.h>

using namespace std;

typedef long double ld;
ld a,b,c,art,dn[1100000],ar[1100000];
int N;

int main(){
	scanf(" %d",&N);
	for(int qw=1;qw<=N;qw++){
		scanf(" %Lf %Lf %Lf",&a,&b,&c);
		art=2.00;
		for(int i=1;i<=1000000;i++){
			dn[i]=dn[i-1]+a/art;
			art+=b;
		}
		art=2.00;
		ar[0]=c/art;
		for(int i=1;i<=1000000;i++){
			art+=b;
			ar[i]=dn[i]+c/art;
		}
		for(int i=1;i<=1000000;i++){
			if(ar[i]>ar[i-1]){
				printf("Case #%d: %.7Lf\n",qw,ar[i-1]);
				break;
			}
		}
	}
	return 0;
}
