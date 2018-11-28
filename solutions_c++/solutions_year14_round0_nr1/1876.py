#include <stdio.h>
#include <vector>

using namespace std;

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-output0.out","w",stdout);
	int tc,count = 0;
	scanf("%d",&tc);
	
	while (tc--) {
		int a,n;
		vector <int> check = vector <int> (17,0);
		for (int k = 0; k < 2; k++) {
			scanf("%d",&a);
			for (int i = 0; i < 4 ; i++) {
				for (int j = 0; j < 4; j++) {
					scanf("%d",&n);
					if (i == a - 1) check[n]++;
				}
			}
		}
		int countTwo = 0, card = -1;
		for (int i = 1; i <= 16; i++) 
			if (check[i] == 2) {
				if (card == -1) card = i;
				countTwo++;
			}
		if (countTwo >= 2) printf("Case #%d: Bad Magician!\n",++count);
		else if (countTwo == 1) printf("Case #%d: %d\n",++count,card);
		else printf("Case #%d: Volunteer cheated!\n",++count);		
	}
}
