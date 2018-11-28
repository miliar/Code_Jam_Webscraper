#include <stdio.h>
using namespace std;
int s;
char shy[1010];
int main(){
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(int ind=1; ind<=t; ind++){
		printf("Case #%d: ", ind);
		scanf("%d %s", &s, shy);
		int p = 0;
		int stood = 0;
		int invite = 0;
		for(int i=0; i<=s; i++){
			int si = shy[i]-'0';
			if(si!=0){
				if(i>stood){
					invite+=(i-stood);
					stood+=(i-stood);
				}
			}
			stood+=si;
		}
		printf("%d\n", invite);
	}
	return 0;
}