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
#define VVI vector<VI>

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/B_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/B_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		int B;
		LL M;
		scanf("%d %lld", &B, &M);
		printf("Case #%d: ", casenum);
		if(1LL<<(B-2) < M){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("POSSIBLE\n");
			VVI v(B,VI(B,0));
			for(int i=0;i<B;i++){
				for(int j=i+1;j<B-1;j++){
					v[i][j] = 1;
				}
			}
			for(int i=B-2;i>0;i--){
				if(1LL<<(i-1) <= M){
					v[i][B-1] = 1;
					M -= 1LL<<(i-1);
				}
			}
			if(M>0){
				v[0][B-1] = 1;
				M--;
			}
			for(int i=0;i<B;i++){
				for(int j=0;j<B;j++){
					printf("%d", v[i][j]);
				}
				printf("\n");
			}
		}
		//cout<<"Case #"<<casenum<<": "<<endl;
	}

	return 0;
}
