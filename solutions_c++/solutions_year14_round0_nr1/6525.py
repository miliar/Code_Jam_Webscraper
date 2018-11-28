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

typedef long long ll;
#define INF (1<<29)

int main(){
	int x, t;
	cin >> t;
	REP(x,t){
		int i, j, id, a[4][4], b[4], c[4], ans;
		cin >> id;
		REP(i,4){
			REP(j,4){
				cin >> a[i][j];
				if(i==id-1)b[j]=a[i][j];
			}
		}
		cin >> id;
		REP(i,4){
			REP(j,4){
				cin >> a[i][j];
				if(i==id-1)c[j]=a[i][j];
			}
		}
		int cnt=0;
		REP(i,4)
			REP(j,4)
				if(c[i]==b[j]){
					cnt++;
					ans=c[i];
				}
		cout << "Case #" << x+1 << ": ";
		if(cnt==0)cout << "Volunteer cheated!" << endl;
		else if(cnt==1)cout << ans << endl;
		else cout << "Bad magician!" << endl;
	}
	return 0;
}

