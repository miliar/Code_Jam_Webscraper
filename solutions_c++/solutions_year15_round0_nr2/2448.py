#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp make_pair
#define go(i,n) for(int i=0;i<n;i++)
#define go3(i,j,n) for(int i=j;i<n;i++)

int a[1001];

int d;

int a1(){
	int ans = 0;
	go(i,d)
	  ans = max(ans, a[i]);

	go3(i,1,1001) {			
			priority_queue<int> q;
			go(j,d)
			  q.push(a[j]);
			
			int la = i;
			go(j,i) {
				int c = q.top(); q.pop();				
				if(c == 1) 
					break;

				if(c > 1) {
					q.push( c/2);
					q.push( (c+1) / 2);
				}
			}

			la += q.top();
			ans = min(ans, la);
		}
	return ans;
}

int a2(){

	int ans = 5000;

	go3(i,1,1001) {
		int la = i;
		go(j,d) {
		  la += (a[j] - 1) / i;
		}
		//cout<<i<<" "<<la<<endl;
		ans = min(ans, la);		  
	}

	return ans;
}

void oku(){
	int T;
	scanf("%d",&T);

	int p;

	go(cs,T){
		scanf("%d",&d);

		go(i, d) {
			scanf("%d",&p);
			a[i] = p;
		}

		int ans = min(a1(),a2());	

		printf("Case #%d: %d\n", cs+1, ans);
	}

}

int main(){
	oku();

	return 0;
}