#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#define eps 10e-6
using namespace std;
int main(){
	freopen("Cokie.txt", "r", stdin);
	freopen("CokieOut.txt", "w", stdout);
	int t, sq = 1;
	cin >> t;
	while (t--){
		double c, f, x;
		cin >> c >> f >> x;

			double tt=100000, ntt=0, tc=2, ntc, nntc, tmp=1000001;
			
			double sum = 0;
			while (true){
				double ntc=(c / tc);
				tc = tc + f;
				//cout << tc << " " << ntc << endl;
				tmp = tt;
				tt = 0;
				tt = sum + ntc + (x / tc);
				sum = tt;
				sum -= (x / tc);
				//cout << "==" << sum << "  " << tt << "    " << tmp << endl;
				if (tt>=tmp) break;
			}
			if ((x/2)<tmp)
				printf("Case #%d: %.7lf\n", sq++, x/2);
			else
				printf("Case #%d: %.7lf\n", sq++, tmp);
		}
	return 0;
}