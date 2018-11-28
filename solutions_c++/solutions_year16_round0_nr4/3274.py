#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAX_N=110;

int T,k,c,s,cases=0;

int main()
{
	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("Dout.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",++cases);
		for(int i=1;i<=s;i++){
			printf(" %d",i);
		}
		printf("\n");
	}
	return 0;
}
