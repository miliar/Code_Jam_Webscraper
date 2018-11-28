#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
using namespace std;

int m[4][4];

int main(){
	set<int> s;
	int ncases, a, b, i, j, cont, ans;
	scanf("%d",&ncases);

	for(int nc=1; nc<=ncases; nc++){
		s.clear();

		scanf("%d",&a); a--;
		for(i=0; i<4; i++)
			for(j=0; j<4; j++){
				scanf("%d",&m[i][j]);
			}
		for(j=0; j<4; j++)
			s.insert(m[a][j]);

		scanf("%d",&b); b--;
		for(i=0; i<4; i++){
			for(j=0; j<4; j++)
				scanf("%d",&m[i][j]);
		}

		cont = 0;
		for(j=0; j<4; j++)
			if(s.count(m[b][j])){
				ans = m[b][j];
				cont++;
			}
		
		printf("Case #%d: ",nc);
		switch(cont){
			case 0:
				printf("Volunteer cheated!\n");
				break;
			case 1:
				printf("%d\n",ans);
				break;
			default:
				printf("Bad magician!\n");
				break;
		}
	}

	return 0;
}
