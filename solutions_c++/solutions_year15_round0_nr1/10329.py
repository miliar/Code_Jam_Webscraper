#include <cstdio>
#include <string>

using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		int max;
		char input[1005];
		scanf("%d",&max);
		scanf("%s",input);
		int tab[1005];
		for(int j=0;j<=max;j++){
			tab[j]=input[j]-'0';
		}
		int sum=0, friends=0;
		int k=0;
		while(k<=max){
			if(tab[k]>0 && sum<k){
				friends+=(k-sum);
				sum+=friends;
			}
			sum+=tab[k];
			k++;
		}
		printf("Case #%d: %d\n",i,friends);
	}
	return 0;
}
