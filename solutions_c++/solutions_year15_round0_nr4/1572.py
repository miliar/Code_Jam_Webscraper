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

int main(){

	int T;
	scanf("%d",&T);
	int x,r,c;
	bool ret;

	go(cs,T) {
		//scanf("%d%d%d",&x,&r,&c);
		cin>> x >> r >> c;
		ret = 0;

		if(r < c) swap(r,c);

		if(x == 1)
			ret = 1;
		else if(x==2) {
			ret = (r % 2 == 0 ) || (c % 2 == 0);
		} else if(x==3) {
			if(r == 3 && c == 2) ret = 1;
			if(r == 4 && c== 3) ret = 1;
			if(r==3 && c==3) ret = 1;
		} else if(x == 4) {
			if(r==4 && c==4) ret = 1;
			if(r==4 && c==3) ret = 1;
		}

		printf("Case #%d: ", cs+1); 
		cout<< (ret ? "GABRIEL" : "RICHARD")<<endl;

	}


	return 0;
}