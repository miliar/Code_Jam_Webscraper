#include <cstdio>
int main(){
	int T;
	scanf("%d",&T);
	for(int caseNumber=0;caseNumber<T;++caseNumber){
		int a1,a2,s1[4][4],s2[4][4];
		scanf("%d",&a1);
		--a1;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j) scanf("%d",&(s1[i][j]));
		scanf("%d",&a2);
		--a2;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j) scanf("%d",&(s2[i][j]));
		int cnt=0,lasthit;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				if(s1[a1][i]==s2[a2][j]){
					++cnt;
					lasthit=s1[a1][i];
				}
		printf("Case #%d: ",caseNumber+1);
		if(cnt==0){
			printf("Volunteer cheated!");
		}else if(cnt==1){
			printf("%d",lasthit);
		}else printf("Bad magician!");
		printf("\n");
	}
}
