#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T,N;

char str[1000][1000];
int reps[1000][1000];
int len[1000],lenS,lenS2;
char S[1000];
bool ok;
int ans;

int main(){
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		lenS=0;
		ans=0;
		ok=true;
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			lenS2=0;
			scanf("%s",str[i]);
			len[i] = strlen(str[i]);
			//printf("string %s len %d\n",str[i],len[i]);
			for(int j=0;j<len[i];j++){
				if(j==0 || str[i][j]!=str[i][j-1]){
					if(i==0){
						S[lenS++]=str[i][j];
						lenS2++;
					}
					else{
						if(lenS2+1>lenS || S[lenS2++]!=str[i][j]) ok=false;
					}
					//printf("i j %d %d\n",i,j);
					reps[i][lenS2-1]=1;
				}
				else{
					reps[i][lenS2-1]++;
				}
			}
			//for(int j=0;j<lenS;j++) printf("i j %d %d %d\n",i,j,reps[i][j]);
			if(i!=0 && lenS != lenS2) ok=false;
		}
			printf("Case #%d: ",t);
			if(!ok) printf("Fegla won\n");
			else{
				for(int i=0;i<lenS;i++){
					int nowmin=1000000000;
					for(int k=1;k<=100;k++){
						int now=0;
						for(int j=0;j<N;j++){
							now += abs(reps[j][i]-k);
						}
						nowmin=min(nowmin, now);
					}
					ans+=nowmin;
				}
				printf("%d\n",ans);
		}
	}
	
	return 0;
}