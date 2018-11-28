#include<cstdio>

using namespace std;
/*
bool palin(int n){
	char s[10];
	int l = sprintf(s,"%d",n);	
	for(int i=0;i<l/2;++i){
		if(s[i] != s[l-i-1])
			return false;
	}
	return true;
}
*/

main(){
	int T,A,B,cont,caso = 1;
	/*for(int i=1;i<32;++i){
		n = i*i;
		if(palin(n) && palin())
			s.insert(n);
		printf("%d = %d\n",i,n);
	}*/

	scanf("%d",&T);
	while(T--){
		cont = 0;
		scanf("%d %d",&A,&B);
		if(A == 1) cont++;
		if(4 >= A && 4 <=B) cont++;
		if(9 >= A && 9 <=B) cont++;
		if(121 >= A && 121 <=B) cont++;
		if(484 >= A && 484 <=B) cont++;
		printf("Case #%d: %d\n",caso++,cont);
		/*for(int i=A;i<=B;++i){
			int num = i*i;
			if(palin(num)){
				cont++;
			}
		}*/
	}
}
