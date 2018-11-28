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

bool can(int x, string s){
	go(i,sz(s))
	  if( i <= x)
	  	x+=s[i]-'0';
	  else
	  	return 0;

return 1;
}

void oku(){
	int T;
	scanf("%d",&T);
	string s, n;

	go(cs, T){
		cin >> n>>s;

		for(int i=0;i<10000;i++)
			if(can(i, s)) {
				printf("Case #%d: %d\n", cs+1 , i);
				break;
			}
	}
}

int main(){

	oku();

	return 0;
}