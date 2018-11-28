#include<iostream>
#include<cstdio>
#include<vector> 
using namespace std;
int t,n,j,cnt,tot;
int b[33];
void work(int depth){
	if (tot==500) return ;
	if (depth==31){
		if (cnt%2==0){
			tot++;
			for (int i=32;i>0;i--)
				printf("%d",b[i]);
			for (int i=2;i<=10;i++)
				printf(" %d",i+1);
			printf("\n");
		}
		return ;
	}
	b[depth] = 1;
	cnt++;
	work(depth+1);
	cnt--;
	b[depth] = 0;
	if (cnt%2==1) return ;
	work(depth+1);
}
int main(){
/*	freopen("skj.in", "r", stdin);*/
	freopen("skj.out", "w", stdout);
	printf("Case #1:\n");
	b[32] = 1;
	b[31] = 1;
	b[1] = 1;
	cnt = 1;
	tot=0;
	work(2);
} 
