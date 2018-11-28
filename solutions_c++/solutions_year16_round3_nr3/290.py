#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
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
#define TI pair<PI,int>
#define VTI vector<TI>

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/C_input1.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/C_output1.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		int J,P,S,K;
        scanf("%d %d %d %d", &J, &P, &S, &K);
        VTI v;
        for(int i=1;i<=J;i++){
			for(int j=1;j<=P;j++){
				for(int k=1;k<=S;k++){
					v.PB(MP(MP(i-1,j-1),k-1));
				}
			}
        }
		int n = J*P*S;
		int best = 0;
		int key = -1;
		int w1[J][P],w2[J][S],w3[P][S];
		for(int i=(1<<n)-1;i>0;i--){
			int bits = __builtin_popcount(i);
			if(bits <= best)
				continue;
			for(int i=0;i<J;i++) for(int j=0;j<P;j++) w1[i][j] = 0;
			for(int i=0;i<J;i++) for(int j=0;j<S;j++) w2[i][j] = 0;
			for(int i=0;i<P;i++) for(int j=0;j<S;j++) w3[i][j] = 0;

			bool good = true;
			for(int j=0;j<n;j++){
				if(i & (1<<j)){
					w1[v[j].F.F][v[j].F.S]++;
					w2[v[j].F.F][v[j].S]++;
					w3[v[j].F.S][v[j].S]++;
					if(max(max(w1[v[j].F.F][v[j].F.S],w2[v[j].F.F][v[j].S]),w3[v[j].F.S][v[j].S]) > K)
					{
						good = false;
						break;
					}
				}
			}
			if(good){
				best = bits;
				key = i;
			}
		}
		printf("Case #%d: %d\n", casenum, best);
		for(int i=0;i<n;i++){
			if(key & (1<<i)){
				printf("%d %d %d\n", v[i].F.F+1, v[i].F.S+1, v[i].S+1);
			}
		}
		//cout<<"Case #"<<casenum<<": "<<endl;
	}

	return 0;
}
