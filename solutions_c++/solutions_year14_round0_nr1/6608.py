#include<algorithm>
#include<bitset>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<deque>
#include<fstream>
#include<functional>
#include<iomanip>
#include<iostream>
#include<list>
#include<map>
#include<numeric>
#include<set>
#include<stack>
#include<string>
#include<utility>
#include<vector>
using namespace std;

#define f(i,n) for(i=0;i<n;++i)

int main() {
	
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	
	int i,j,tc,t,ga[4][4],gb[4][4],a,b,k,card;
	scanf("%d",&t);
	for(tc=1;tc<=t;++tc) {
		scanf("%d",&a);
		f(i,4) f(j,4) scanf("%d",&ga[i][j]);
		scanf("%d",&b);
		f(i,4) f(j,4) scanf("%d",&gb[i][j]);
		--a;
		--b;
		k=0;
		f(i,4) {
			f(j,4) {
				if(ga[a][i]==gb[b][j]) {
					++k;
					card=ga[a][i];
				}
			}
		}
		printf("Case #%d: ",tc);
		if(!k) printf("Volunteer cheated!\n");
		else if(k==1) printf("%d\n",card);
		else printf("Bad magician!\n");
	}
}

