#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++){
		int fi;
		scanf("%d",&fi);
		vector<int> firstSelect(4);
		for(int i=1; i<=4; i++){
			vector<int> tmp(4);
			for(int j=0; j<4; j++)
				scanf("%d", &tmp[j]);
			if(i == fi)
				firstSelect = tmp;
		}

		int si;
		scanf("%d",&si);
		for(int i=1; i<=4; i++){
			vector<int> tmp(4);
			for(int j=0; j<4; j++)
				scanf("%d",&tmp[j]);

			if(i == si){
				// determine answer

				vector<bool> found(4,false);
				int fc = 0;
				for(int j=0; j<4; j++){
					for(int k=0; k<4; k++)
						if(firstSelect[j] == tmp[k]){
							found[j] = true;
							fc++;
						}
				}
				printf("Case #%d: ",tc);
				switch(fc){
				case 1:
					for(int j=0; j<4; j++)
						if(found[j])
							printf("%d\n", firstSelect[j]);
					break;
				case 0:
					printf("Volunteer cheated!\n");
					break;
				default:
					printf("Bad magician!\n");
				}
			}
		}
	}
}