#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
#define INF (1<<29)

int main(){
	int x, r, c, tc;
	cin >> tc;
	for(int i=0;i<tc;i++){
		cin >> x >> r >> c;
		if(r>c)swap(r,c);
		string ans="GABRIEL";
		if(x==1){
			ans="GABRIEL";
		}
		else if(x==2){
			if((r*c)%2==1)ans="RICHARD";
		}
		else if(x==3){
			if((r*c)%3==0)ans="GABRIEL";
			else ans="RICHARD";
			if(r*c==3)ans="RICHARD";
		}
		else{
			if((r==3&&c==4)||(r==4&&c==4))ans="GABRIEL";
			else ans="RICHARD";
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}

