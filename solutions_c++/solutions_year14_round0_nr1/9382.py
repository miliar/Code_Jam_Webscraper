#include <bits/stdc++.h>
using namespace std;

#define s(n)                        scanf("%d",&n)
int main(int argc, char const *argv[])
{
	int T;
	s(T);
	for(int i=1;i<=T;++i){
		printf("Case #%d: ",i);
		int r1,r2;
		s(r1);
		vector<int> a(17);
		vector<int> b(17);
		int c[4][4];
		int d[4][4];
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				s(c[i][j]);
			}
		}
		s(r2);
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j){
				s(d[i][j]);
			}
		}
		--r1;
		--r2;
		for(int i=0;i<4;++i){
			a[c[r1][i]]=1;
			b[d[r2][i]]=1;
		}
		int co=0;
		int card=-1;
		for(int i=1;i<=16;++i){
			if(a[i]==b[i] && a[i]==1){
				++co;
				card=i;
			}
		}
		if(co==1){
			printf("%d\n",card);
			continue;
		}
		if(co>1){
			printf("Bad magician!\n");
			continue;
		}
		if(co==0){
			printf("Volunteer cheated!\n");
		}
	}
	return 0;
}