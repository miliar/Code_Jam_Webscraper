#include <cstdio>
#include <algorithm>

using namespace std;

void resoud(){
	int y1,y2,v;
	bool vu[17];
	fill(vu,vu+17,false);
	scanf("%d",&y1);
	for (int y=0;y<4;y++)
		for (int x=0;x<4;x++){
			scanf("%d",&v);
			if (y==y1-1)
				vu[v]=true;
		}
	scanf("%d",&y2);
	int sol=0,nbSol=0;
	for (int y=0;y<4;y++)
		for (int x=0;x<4;x++){
			scanf("%d",&v);
			if (y==y2-1 && vu[v]){
				nbSol++;
				sol=v;
			}
		}
	if (nbSol==0)
		puts("Volunteer cheated!");
	else if (nbSol==1)
		printf("%d\n",sol);
	else puts("Bad magician!");
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		printf("Case #%d: ",i);
		resoud();
	}
	return 0;
}
