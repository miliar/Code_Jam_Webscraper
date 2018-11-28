#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
float C, F, X, s, g;
int main(){
	int T;
	scanf("%d",&T);
	for(int ix = 1; ix <= T; ix++){
		vector<float> sols;
		double gs = 2;
		double t = 0;
		double tg = 0;
		double nuevo = 0;
		double previo = 0;
		bool prim =  true;
		scanf("%f%f%f", &C, &F, &X);
		while(true)
		{
			nuevo = tg;
			tg = (X / gs) + t;
			previo = tg;
			if(nuevo < previo && !prim) break;
			t += C / gs;
			gs += F;
			prim = false;
		}
		//sort(sols.begin(), sols.end());
		printf("Case #%d: %.7f\n",ix,nuevo);
	}
	return 0;
}