#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int getlog(int X){
	int cnt=0;
	while(X){
		X>>=1;
		cnt++;
	}
	return cnt;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N;
	int SMax;
	int ans=0,ansc;
	scanf("%d",&T);

	for(int t=1;t<=T;t++){
		ans=99999999;
		int input[1010]={0,};
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			scanf("%d",&input[i]);
		}
		for(int i=1;i<1010;i++){
			int c=i;
			for(int j=0;j<N;j++){
				if(input[j] > i) c+=(input[j]-1)/i;
			}
			ans=min(ans,c);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}