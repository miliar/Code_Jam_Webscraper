#include <cstdio>
using namespace std;

int main(){
	int sum, tot, ivt, sm, ppl, i, T, s;
	char sp [1001];
	scanf("%d\n", &T);
	for(i=1;i<=T;i++){
		scanf("%d %s",&sm, &sp);
		sum=0;
		tot=0;
		for(s=0;s<=sm;s++){
			ppl = sp[s]- '0';
			tot+=ppl;
			if(sum<=s){
				sum=s+ppl;
			}
			else sum=sum+ppl;
		}
		ivt=sum-tot;
		scanf("\n");
		printf("Case #%d: %d\n", i, ivt);
	}
	
}
