#include <cstdio>
#include <cstring>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
char S[1001];
int main() {
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++) {
		int Smax;
		scanf("%d %s",&Smax,S);
		int sum=0,ans=0;
		for(int j=0;j<Smax;j++) {
			sum+=S[j]-'0';
			if(sum<(j+1)) {
				ans+=(j+1-sum);
				sum=j+1;
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}