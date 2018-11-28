#include<cstdio>
#include<set>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int c = 1; c<=t; c++) {
		int f, s, x,  p = 0, ret = -1;
		set<int> S;
		scanf("%d", &f); f--;
		for(int i=0; i<4; i++)
			for(int j=0;j<4;j++){
				scanf("%d", &x);
				if(i == f)
	        S.insert(x);
			}
		scanf("%d",&s); s--;
		for(int i=0; i<4; i++)
			for(int j=0;j<4;j++){
				scanf("%d", &x);
				if(i == s) 
			    if(S.count(x)){
				    p++;
				    ret = x;
			    }
			}
		if(p==0)
			printf("Case #%d: Volunteer cheated!\n", c);
		else if (p==1)
			printf("Case #%d: %d\n", c, ret);
		else printf("Case #%d: Bad magician!\n", c);
	}
	return 0;
}
