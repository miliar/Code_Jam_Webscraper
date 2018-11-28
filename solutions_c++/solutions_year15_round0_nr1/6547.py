//wawando's template

#include <iostream>
#include <string>
#include <fstream>
#include <functional>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <list>
#include <set>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>  //clock_t , clock() , CLOCKS_PER_SEC
#include <cstring>
#include <cctype>
#include <climits> // LLONG_MAX , LLONG_MIN , INT_MAX , INT_MIN

//MACROS
#define pb              push_back
#define mp              make_pair
#define INF             1000000000     //1 billion safer for floyd warshall, avoid overflow
		
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;

int TC,caseNo = 1;

int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	//ios::sync_with_stdio(false);
	scanf("%d",&TC);
	while(TC--){
		int currentStand = 0, friendNeeded = 0;
		int smax,si;
		char csi[1010];
		scanf("%d ",&smax);
		gets(csi);
		for(int i = 0; i <= smax; i++){
			si = csi[i] - '0';
			//printf("%d\n",currentStand);
			if(si > 0){
				if(currentStand >= i)
					currentStand += si;
				else {
					int tempFriendNeeded = i - currentStand;
					currentStand += (tempFriendNeeded + si);
					friendNeeded += tempFriendNeeded;
				}
			}
		}
		printf("Case #%d: %d\n",caseNo++, friendNeeded);
	}
	return 0;
}
