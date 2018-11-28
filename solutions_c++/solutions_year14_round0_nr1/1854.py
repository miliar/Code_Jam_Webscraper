#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>

using namespace std;
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();++itr)
#define X first
#define Y second
#define PB push_back
#define MP make_pair
int t,cnts[20];
int main() {
	int Z;
	cin>>Z;
	rep(z,Z){
		int res=0,rt;
		memset(cnts,0,sizeof(cnts));
		int a,b;
		cin>>a;
		rep(i,4)rep(j,4){
			cin>>t;
			if(i==a-1)cnts[t]=1;
		}
		cin>>b;
		rep(i,4)rep(j,4){
			cin>>t;
			if(i==b-1&&cnts[t]){
				++res;
				rt=t;
			}
		}
		printf("Case #%d: ", z+1);
		if(res==0)printf("Volunteer cheated!\n");
		else if(res==1)printf("%d\n", rt);
		else printf("Bad magician!\n");
	}
 	return 0;
}
