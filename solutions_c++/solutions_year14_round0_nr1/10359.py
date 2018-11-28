#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main(){

	int N,K,cnt,a;
	int ar1[20],ar2[20];

	scanf(" %d",&N);
	
	for(int i=1;i<=N;i++){
		
		cnt=0;
		memset(ar1,0,sizeof(ar1));
		memset(ar2,0,sizeof(ar2));
		
		scanf(" %d",&K);
		
		for(int j=0;j<16;j++){
			scanf(" %d",&a);
			if(j/4==K-1)
				ar1[a]=1;
		}
		
		scanf(" %d",&K);
		
		for(int j=0;j<16;j++){
			scanf(" %d",&a);
			if(j/4==K-1)
				ar2[a]=1;
		}
		
		for(int j=1;j<=16;j++)
			if(ar1[j] && ar2[j])
				cnt++;
		
		if(cnt==1){
			for(int j=1;j<=16;j++)
				if(ar1[j] && ar2[j]){
					printf("Case #%d: %d\n",i,j);
					break;
				}
		}
		else if(!cnt) printf("Case #%d: Volunteer cheated!\n",i);
		else if(cnt>1) printf("Case #%d: Bad magician!\n",i);
	
	}

	return 0;
}
