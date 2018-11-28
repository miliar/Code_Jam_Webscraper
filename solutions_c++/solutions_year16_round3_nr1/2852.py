#include <iostream>
#include <cstdio>
#include <string>
using namespace std; 
struct se
{
	int num;
	char P;
}S[30];
bool cmp(se a, se b){
	return a.num>b.num;
}
void getans(int n){
	if (n == 2){
		while (S[1].num){
			printf("%c%c ",S[1].P,S[2].P);
			S[1].num--;	
		}	
		puts("");
		return;
	}
	while (n>3){
		sort(S+1,S+1+n,cmp);
		printf("%c ",S[1].P);
		S[1].num--;
		if (S[1].num==0) n--;
	}
	sort(S+1,S+1+n,cmp);
	while (S[2].num>S[3].num){
		printf("%c%c ",S[1].P,S[2].P);
		S[1].num--,S[2].num--;
	}
	while (S[1].num){
		printf("%c ",S[1].P);
		S[1].num--;
	}
	while (S[3].num){
		printf("%c%c ",S[2].P,S[3].P);
		S[3].num--;			
	}
	puts("");
	return;
}
int main(){
	int T,n;
	freopen("A-small-attempt0.in.txt","r",stdin); 
	freopen("A-small-attempt0.out.txt","w",stdout); 
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){ 
		printf("Case #%d: ",cases);  
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			S[i].P='A'+i-1,scanf("%d",&S[i].num); 
		getans(n);
	}
	return 0;
}