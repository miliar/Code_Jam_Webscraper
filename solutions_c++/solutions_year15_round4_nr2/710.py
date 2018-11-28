#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define MEMSET_INF 127
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

double flow[101];
double temp[101];

int main(int argc, char const *argv[]){
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
		int n;
		double v,x;
		cin >> n;
		cin >> v >> x;
		for(int i = 0; i < n; i++){
			cin >> flow[i] >> temp[i];
		}
		double ans = -1.0;
		if(n == 1){
			if(temp[0] == x){
				ans = v/flow[0];
			}
		}else{
			if(temp[0] == x and temp[1] == x){
				ans = v/(flow[0]+flow[1]);
			}else if(temp[0] == x){
				ans = v/flow[0];
			}else if(temp[1] == x){
				ans = v/flow[1];
			}else{
				double mntemp, mnflow, mxtemp, mxflow;
				if(temp[0] > temp[1]){
					mntemp = temp[1];
					mnflow = flow[1];
					mxtemp = temp[0];
					mxflow = flow[0];
				}else{
					mntemp = temp[0];
					mnflow = flow[0];
					mxtemp = temp[1];
					mxflow = flow[1];
				}

				if(mntemp < x and x < mxtemp){
					double ansmin;
					double ansmax;

					double absmin = abs(x - mntemp);
					double absmax = abs(x - mxtemp);

					double ratio = absmin/absmax;

					double mnval = (1.0/(ratio + 1.0))*v;
					double mxval = (ratio/(ratio + 1.0))*v;

					ans = max(mnval/mnflow, mxval/mxflow);
				}

			}
		}
		if(ans != -1.0){
			cout << "Case " << "#" << t << ": " << fixed << setprecision(9) << ans << endl;
		}else{
			cout << "Case " << "#" << t << ": IMPOSSIBLE"<< endl;
		}
	}



    return 0;
}