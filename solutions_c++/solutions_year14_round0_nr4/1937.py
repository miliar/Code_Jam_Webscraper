#include <cstdio>
#include <algorithm>
#include <vector>
using namespace	std;

int main(){
	int T,N;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		scanf("%d",&N);
		double temp;
		vector<double> naomi,ken,naomit,kent;
		for (int x=0;x<N;x++){
			scanf("%lf",&temp);
			naomi.push_back(temp);
		}
		for (int x=0;x<N;x++){
			scanf("%lf",&temp);
			ken.push_back(temp);
		}
		sort(ken.begin(),ken.end());
		sort(naomi.begin(), naomi.end());
		naomit=naomi;
		kent=ken;
		int kp=0,np=0;
		for (int x=0;x<N;x++){
			for (int y=0;y<ken.size();y++){
				if (ken[y]>naomi[x]){
					kp++;
					ken.erase(ken.begin()+y);
					break;
				}
			}
		}
		for (int x=0;x<N;x++){
			for (int y=0;y<naomit.size();y++){
				if (naomit[y]>kent[x]){
					np++;
					naomit.erase(naomit.begin()+y);
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",i,np,N-kp );
	}

}