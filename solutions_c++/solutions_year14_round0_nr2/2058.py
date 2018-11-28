#include <cstdio>
#include <vector>
using namespace std;

int main(){
	int cases, farms;
	double C, F, X, s, ans;
	vector<double> waitT, geneT;
	scanf("%d", &cases);
	for(int ca=1;ca<=cases;++ca){
		printf("Case #%d: ", ca);
		waitT.clear(), geneT.clear();
		scanf("%lf%lf%lf", &C, &F, &X);
		s = 2.0, ans = 0.0;
		geneT.push_back(0.0), waitT.push_back(X/s);
		for(farms=1;;++farms){
			geneT.push_back(C/s);
			s += F;
			waitT.push_back(X/s);
			if(waitT[farms]+geneT[farms]>waitT[farms-1])
				break;
		}
		for(int i=0;i<=farms-1;++i)
			ans += geneT[i];
		ans += waitT[farms-1];
		printf("%.7lf\n", ans);
	}
}
