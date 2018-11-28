#include <bits/stdc++.h>
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;



double C1, C2, R1, R2, X, V, alpha;

void I(){
	cout << "IMPOSSIBLE" << endl;
}


int main (){
	int tt; cin >> tt;
	f (kase, 1, tt+1){
		int n; cin >> n >> V >> X;
		cin >> R1 >> C1;
		bool ok = 0;
		printf("Case #%d: ", kase);
		if (n == 1){
			if (C1 != X){
				I();
			}
			else{
				printf("%.10f\n", V/R1);
			}
		}
		else{
			cin >> R2 >> C2;
			if (X < min(C1, C2) || X > max(C1, C2)) I();
			else{
				if (C1 == C2){
					double ini = 0, fim = 10e15;
					f (vz, 0, 200){
						double mid  = 0.5*(ini+fim);
						if (R1*mid + R2*mid > V) fim = mid;
						else ini = mid;
					}
					printf("%.10f\n", ini);
				}
				else{
					alpha = (X-C2)/(C1-C2);
					double t1 = (alpha*V)/R1;
					double t2 = ((1.-alpha)*V)/R2;
					printf("%.10f\n", max(t1, t2));
				}
			}
		}

	}
	return 0;
}
