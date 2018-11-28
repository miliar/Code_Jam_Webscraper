#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<string>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define VB vector<bool>
#define VI vector<int>
#define VLL vector<LL>
#define VPI vector<PI>
#define PB push_back
#define VVI vector<VI>
#define VD vector<double>

int N,K;

VD prod(VD cur,double p){
	VD res(K+1,0.0);
	for(int i=0;i<=K;i++){
		if(i > 0){
			res[i] += p*cur[i-1];
		}
		res[i] += (1.0-p)*cur[i];
	}
	return res;
}

double tie(VD z){
	VD res(K+1,0.0);
	res[0] = 1.0;
	for(int i=0,sz=z.size();i<sz;i++){
		res = prod(res,z[i]);
	}
	return res[K/2];
}

int main()
{
	freopen("B_input2.txt", "r", stdin);
	freopen("B_output2v.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		scanf("%d %d", &N, &K);
		VD v;
		for(int i=0;i<N;i++){
			double tmp;
			cin>>tmp;
			v.PB(tmp);
		}
		sort(v.begin(), v.end());
		double best = 0.0;
		for(int l=0;l<=K;l++){
			VD z;
			
			for(int i=0;i<l;i++){
				z.PB(v[i]);
			}

			for(int i=0;i<K-l;i++){
				z.PB(v[N-1-i]);
			}

			best = max(best,tie(z));
		}
		printf("Case #%d: %.8lf\n", casenum, best);
//		cout<<"Case #"<<casenum<<": "<<setprecision(8)<<best<<endl;
	}

	return 0;
}
