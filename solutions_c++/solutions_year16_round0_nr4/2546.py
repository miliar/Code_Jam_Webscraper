#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen ("myfile.txt","w",stdout);
	
	int t,i,j;
	long long pen,k,c,s,pan,bil;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%lld %lld %lld",&k,&c,&s);
		pan=c-1;
		pen=1;
		bil=k;
		if(pan==0)bil=1;
		while(pan>1){
			if(pan%2==1){
				pen*=bil;
			}
			pan/=2;
			bil=bil*bil;
		}
		bil*=pen;
		printf("Case #%d:",i+1);
		for(j=1;j<=k;j++){
			printf(" %lld",j*bil);
		}
		printf("\n");
	}
	
	fclose (stdout);
}
