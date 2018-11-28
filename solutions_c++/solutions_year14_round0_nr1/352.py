#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <stack>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
unsigned long long one = 1;

int t;
int a,b,ans,x;
int bitmask;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		bitmask = 0;
		scanf("%d",&a);
		a--;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				scanf("%d",&b);
				if (i == a) bitmask |= (1<<b);
			}
		}
		x = 0;
		ans = -1;
		scanf("%d",&a);
		a--;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				scanf("%d",&b);
				if (i == a){
					if (bitmask & (1<<b)){
						x++;
						ans = b;
					}
				}
			}
		}
		printf("Case #%d: ",jj);
		if (x == 1) printf("%d\n",ans);
		else if (x > 1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
