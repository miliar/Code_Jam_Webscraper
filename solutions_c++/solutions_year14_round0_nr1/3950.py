#include <cstdio>
#include <cstring>

using namespace std;

	int t,r,card,tmp,q;
	bool deck[17];

int main() {
	
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("Output.in","w",stdout);
	scanf("%d",&t);
	for (int k=1; k<=t; k++) {
		q = 0;
		scanf("%d",&r);
		memset(deck,0,17*sizeof(bool));
		for(int i=1; i<=4; i++) {
			for(int j=1; j<=4; j++) {
				scanf("%d",&tmp);
				if (i == r) deck[tmp]++;
			}
		}
		scanf("%d",&r);
		for(int i=1; i<=4; i++) {
			for(int j=1; j<=4; j++) {
				scanf("%d",&tmp);
				if (i == r) {
					if (deck[tmp]) {
						q++;
						card = tmp;
					}
				}
			}
		}
		if (q == 0) printf("Case #%d: Volunteer cheated!\n",k);
		else if (q == 1) printf("Case #%d: %d\n",k,card);
		else printf("Case #%d: Bad magician!\n",k);
	}

	return 0;
}
