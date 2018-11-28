#include <bits/stdc++.h>

#define MAX 1010

using namespace std;
typedef long long int ll;

int T,D,aux;
int P[MAX];

int main(){
	scanf("%d",&T);
	for(int caso=1;caso<=T;caso++){
		scanf("%d",&D);
		for(int i=0;i<D;i++) scanf("%d",&P[i]);
		sort(P,P+D);
		reverse(P,P+D);		
		int resp=P[0];		
		for(int i=1;i<=P[0];i++){
			int atual=i;
			for(int j=0;j<D;j++){
				atual+=P[j]/i -1;
				if(P[j]%i) atual++;			
			}
			resp=min(resp,atual);	
		}				
		printf("Case #%d: %d\n",caso,resp);	
	}
}
