#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int M,N;
char s[1024][101];
char *p[1024];
bool myfunction (char* i,char* j) { return strcmp(i,j) > 0; }


int com[1024];
int ans = -1;
int cou = 0;
int suffixCom(char *i, char *j){
	int il = strlen(i);
	int jl = strlen(j);
	
	int ii = 0;
	int ji = 0;
	while(ii < il && ji < jl){
		char a = i[ii];
		char b = j[ji];

		if(a != b)break;
		ii++;
		ji++;
	}
	return (jl - ji);

}
int d(int l){
	if(l == M){
		int sum = 0;
		for(int mi=0;mi<N;mi++){
			char * pre = 0;
			int flag = 0;
			for(int si = 0; si < M;si++){
				if(com[si] == mi){
					flag = 1;
					if(pre == 0){
						sum += strlen(p[si]);
					}else{
						sum += suffixCom(pre, p[si]);
					}
					pre = p[si];

				}
			}
			if(flag == 1)
				sum++;
		}
		if(sum == ans)cou++;
		else if(sum > ans){
			ans = max(sum, ans);
			cou = 1;
		}
		
		
		return 0;
	}
	for(int i=0;i<N;i++){
		com[l] = i;
		d(l + 1);
	}
	return 0;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int ca = 1; ca <=T ;ca++){
		scanf("%d %d",&M,&N);
		ans = -1;
		for(int i=0;i<M;i++){
			scanf("%s",s[i]);
			p[i] = s[i];
		}


		sort(p, p + M, myfunction);
		d(0);


		

		printf("Case #%d: ",ca);
		printf("%d %d\n",ans,cou);
	}
	return 0;
}
