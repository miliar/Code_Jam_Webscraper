#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <numeric>
#include <functional>
#include <cmath>

#define rep2(x,fr,to) for(int (x)=(fr);(x)<(to);(x)++)
#define rep(x,to) for(int (x)=0;(x)<(to);(x)++)
#define repr(x,fr,to) for(int (x)=(fr);(x)>=(to);(x)--)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

using namespace std;
typedef long long ll; typedef vector<int> VI;
typedef pair<int,int> pii;


void fnc00(int n, int qt){
	if(n==0){ printf("Case #%d: INSOMNIA\n", qt+1); return;}
	vector<char> tn(10, 0);
	int lst=-1;
	for(int p=1;;p++){
		lst = n*p;
		for(int w = lst;w>0;w /=10){
			tn[w%10] =1;
		}
		if(accumulate(all(tn), 0)>=10) break;
	}
	printf("Case #%d: %d\n", qt+1, lst);

}

int main()
{
	int t; cin >> t;
	rep(qt,t){
		int n; cin >>n;
		fnc00(n, qt);
	}
	
	return 0;
}
