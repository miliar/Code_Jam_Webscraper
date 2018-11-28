#include <cstdio>
#include <string>
using namespace std;

int main(){
	string sample_i {"sample"};
	string small_i {"B-small-attempt1"};
	string large_i {"B-large"};
	freopen((large_i+".in").c_str(), "r", stdin);
	freopen((large_i+".out").c_str(), "w", stdout);
	int N;
	double c, f, x, t, m;
	scanf("%6d", &N);
	for(int i = 1; i <= N; ++i){
		t = 0;
		m = 2;
		scanf("%lf%lf%lf", &c, &f, &x);
		while(x/(m+f)+c/m < x/m){
			t+=c/m;
			m+=f;
		}
		t+=x/m;
		printf("Case #%d: %.7lf\n", i, t);
	}
	return 0;
}
