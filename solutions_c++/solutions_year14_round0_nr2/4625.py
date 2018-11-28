#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = (a); i < (b); ++i)
#define pb push_back
#define eps 1e-7

using namespace std;
typedef long long ll;

int main(){
	int t, caso = 1;
	double c, f, x;
	scanf("%d", &t);
	
	while(t--){
		scanf("%lf %lf %lf", &c, &f, &x);
		double atual = 2.0, ans = 0.0;
		while(x/atual - (c/atual + x/(atual+f)) > eps){
			ans += c/atual;
			atual += f;
		}
		
		ans += x/atual;
		printf("Case #%d: %lf\n", caso++, ans);
		
		
		
	}

	return 0;
}

