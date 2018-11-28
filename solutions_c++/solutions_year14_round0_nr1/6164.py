#include <cstdio>
using namespace std;
int A[4][4], B[4][4];
int main(){
	int t,cas,a,b,i,j,acc,v;
	scanf("%d",&t);
	for(cas=1; cas<=t; ++cas){
		scanf("%d",&a);
		for(i=0; i<4; ++i)
			for(j=0; j<4; ++j)
				scanf("%d",&A[i][j]);
		scanf("%d",&b);
		for(i=0; i<4; ++i)
			for(j=0; j<4; ++j)
				scanf("%d",&B[i][j]);
		a--; b--;
		for(v=acc=i=0; i<4; ++i)
			for(j=0; j<4; ++j)
				if(A[a][i]==B[b][j])
					acc++, v=A[a][i];
		if(!acc) printf("Case #%d: Volunteer cheated!\n",cas);
		else if(acc==1) printf("Case #%d: %d\n",cas,v);
		else printf("Case #%d: Bad magician!\n",cas);
	}
	return 0;
}