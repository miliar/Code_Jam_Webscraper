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

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/A_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/A_output2.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		int N;
		scanf("%d", &N);
        VPI v;
        for(int i=0;i<N;i++){
			int p;
			scanf("%d", &p);
			v.PB(MP(p,i));
        }
		printf("Case #%d: ", casenum);
		sort(v.begin(),v.begin()+N,greater<PI>());
		while(N){
			if(v[0].F > v[1].F){
				v[0].F--;
				printf("%c ", char('A'+v[0].S));
			}
			else if(v[0].F == v[1].F and N==2){
				v[0].F--;
				v[1].F--;
				printf("%c%c ", char('A'+v[0].S), char('A'+v[1].S));
			}
			else if(v[0].F == v[1].F and N > 2 and v[1].F > v[2].F){
				v[0].F--;
				v[1].F--;
				printf("%c%c ", char('A'+v[0].S), char('A'+v[1].S));
			}
			else if(v[0].F == v[1].F and N > 2 and v[1].F == v[2].F and v[2].F > 1){
				v[0].F--;
				v[1].F--;
				printf("%c%c ", char('A'+v[0].S), char('A'+v[1].S));
			}
			else if(v[0].F == v[1].F and N > 2 and v[1].F == v[2].F and v[2].F == 1){
				v[0].F--;
				printf("%c ", char('A'+v[0].S));
			}
			else{
				printf("I did not think of this case\n");
			}
			sort(v.begin(),v.begin()+N,greater<PI>());
			while(N > 0 and v[N-1].F==0){
				N--;
			}
		}
		printf("\n");
		//cout<<"Case #"<<casenum<<": "<<endl;
	}

	return 0;
}
