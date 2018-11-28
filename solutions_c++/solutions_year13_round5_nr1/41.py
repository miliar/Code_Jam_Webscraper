#include<vector>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstdlib>
#define MOD
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
using namespace std;
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;
typedef vector<i64> llvec;

int T, N;
i64 B, X[37];
llvec V;

int main()
{
	scanf("%d", &T);

	for(int t=0;t++<T;){
		scanf("%lld%d", &B, &N);
		for(int i=0;i<N;i++) scanf("%lld", X+i); V.clear();
		for(int i=0;i<N;i++) V.push_back(X[i]);
		while(V.size() < 37) V.push_back(0);

		sort(V.begin(), V.end());
		V.push_back(1LL << 60LL);
		
		double ret = 0;
		for(int i=1;i<=35;i++){
			i64 mxHigh = V[i]-1;
			i64 sum = 0;
			for(int j=0;j<i;j++) sum += V[j];
			mxHigh = min(mxHigh, (sum+B)/i);

			//printf("%lld %d\n", mxHigh, i);
			for(int j=0;j<i;j++) if(V[j] > mxHigh) goto nex;

			ret = max(ret, (36.0 / i - 1) * (mxHigh * i - sum));
nex:

			for(int j=0;i+j<V.size();j++){
				//[0, i) 本命 [i, i+j) フェイク
				mxHigh = V[i+j];
				i64 sum2 = 0;
				for(int k=0;k<i+j;k++) sum2 += V[k];

				mxHigh = min(mxHigh, (sum2 + B + i) / (i+j));
				--mxHigh;
				//printf("%d %d: %lld %lld\n", i, j, mxHigh, V[i+j]);
				for(int k=0;k<i+j;k++) if(V[k] > mxHigh) goto nex2;

				//printf("%d %d: %f\n", i, j, 36 * (mxHigh - sum / (double)i) - (mxHigh * (i+j) + j - sum2));
				ret = max(ret, 36 * (mxHigh - sum / (double)i) - (mxHigh * (i+j) + j - sum2));
nex2:
				continue;
			}
		}

		printf("Case #%d: %.10f\n", t, ret);
	}

	return 0;
}
