#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	char S[1005];
	int T,N,i,frnds,sum,j;
	scanf("%d",&T);
	for(j=1;j<=T;j++){
		scanf("%d %s",&N,S);
		frnds=0;
		sum=0;
		for(i=0;i<=N;i++){
			if(sum<i && S[i]!='0'){
				frnds+=(i-sum);
				sum+=frnds;
			}
			sum+=(S[i]-'0');
		}
		printf("Case #%d: %d\n",j,frnds);
	}

	return 0;
}