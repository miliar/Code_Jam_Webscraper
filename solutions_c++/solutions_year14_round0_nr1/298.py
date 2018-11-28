#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <sstream>
#include <functional>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <list>
#include <numeric>
using namespace std;
const double PI = 3.14159265358979323846;
const double EPS = 1e-12;
const int INF = 1<<25;
typedef pair<int,int> P;
typedef long long ll;
typedef unsigned long long ull;


int main(){
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		int d[16];
		memset(d,0,sizeof(d));
		for(int k = 0; k < 2; k++){
			int r;
			cin>>r;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
					int c;
					cin>>c;
					if(i+1==r) d[c-1]++;
				}
			}
		}
		int res = 0, out = -1;
		for(int i = 0; i < 16; i++){
			if(d[i]==2){
				res++;
				out = i+1;
			}
		}
		printf("Case #%d: ",Case);
		if(res==1) printf("%d",out);
		else if(res==0) printf("Volunteer cheated!");
		else printf("Bad magician!");
		puts("");
	}
	return 0;
}

