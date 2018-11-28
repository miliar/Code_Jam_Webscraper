#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int Rr1[4+2];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	int nCase;
	scanf("%d",&nCase);
	for(int nc=1;nc<=nCase;nc++){
		int r1,r2,dump,r2_e;
		scanf("%d",&r1);
		for(int i=0;i<4*(r1-1);i++)scanf("%d",&dump);
		for(int i=0;i<4;i++)scanf("%d",&Rr1[i]);
		for(int i=0;i<4*(4-r1);i++)scanf("%d",&dump);
		vector<int> match;
		scanf("%d",&r2);
		for(int i=0;i<4*(r2-1);i++)scanf("%d",&dump);
		for(int i=0;i<4;i++){
			scanf("%d",&r2_e);
			for(int j=0;j<4;j++)if(Rr1[j]==r2_e)
				match.push_back(r2_e);
		}
		for(int i=0;i<4*(4-r2);i++)scanf("%d",&dump);

		if(match.size()==1)printf("Case #%d: %d\n",nc,match[0]);
		else if(match.size()>1)printf("Case #%d: Bad magician!\n",nc);
		else printf("Case #%d: Volunteer cheated!\n",nc);
	}
	return 0;
}

