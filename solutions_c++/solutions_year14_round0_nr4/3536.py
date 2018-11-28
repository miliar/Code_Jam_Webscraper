#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int w=1; w<=T; w++){
		int N;
		scanf("%d", &N);
		vector<double> Naomi, Ken;
		double weight;
        for(int i=0; i<N; i++){
            scanf("%lf", &weight);
            Naomi.push_back(weight);
        }
        for(int i=0; i<N; i++){
            scanf("%lf", &weight);
            Ken.push_back(weight);
        }
        sort(Naomi.begin(),Naomi.end());
        sort(Ken.begin(),Ken.end());

        //Deceitful War
        int t1 = 0, count = N;
        int Nstart = 0, Kstart = 0, Kend = N-1;
        while(count--){
            if(Naomi[Nstart] < Ken[Kstart]){
                Nstart++;
                Kend--;
            }
            else{
                t1++;
                Nstart++;
                Kstart++;
            }
        }
        //War
        int t2 = 0;
        Nstart = Kstart = 0;
        while( (Nstart < N) && (Kstart < N) ){
            while( Nstart<N && Kstart<N && Naomi[Nstart]>Ken[Kstart] ){
                Kstart++;
            }
            if(Kstart < N && Nstart < N){
                t2++;
                Kstart++;
                Nstart++;
            }
        }
        t2 = N - t2;

        char *c1 = "Case #";
        char *c2 = ": ";
        char *c3 = " ";
		printf("%s%d%s%d%s%d\n", c1, w, c2, t1, c3, t2);
	}

	return 0;
}
