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
	int n, tc, p[100], cnt;
	cin >> tc;
	for(int i=0;i<tc;i++){
		cin >> n;
		cnt=0;
		for(int j=0;j<n;j++){
			cin >> p[j];
			cnt+=p[j];
		}
		cout << "Case #" << i+1 << ":";
		bool check=true;
		int mx, id, it=0;
		while(check){
			mx=0;
			id=-1;
			check=false;
			for(int j=0;j<n;j++){
				if(mx<p[j]){
					mx=p[j];
					id=j;
					check=true;
				}
			}
			if(check){
				p[id]--;
				cnt--;
				if(cnt%2==1||it==0)cout << " ";
				printf("%c",id+'A');
			}
			it++;
		}
		puts("");
	}
	return 0;
}
