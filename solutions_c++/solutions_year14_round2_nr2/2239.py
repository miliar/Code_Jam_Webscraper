#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <math.h>
#include <time.h>
#include <set>
#include <utility>
#include <map>
#include <stdio.h>
#include <assert.h>
#include <limits.h>
 
using namespace std;

 
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef long double ld;
#define var(a,b) __typeof(b) a = b
#define rep(i,n) for(int i = 0;(i) < (n); ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it) for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define all(v) v.begin(),v.end()



int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t;i++){
		int a,b,k;
		int count = 0;
		cin >> a >> b >> k;
		for(int j = 0; j < a; j++){
			for(int l = 0; l < b;l++){
				if((j & l) < k ){
					count++;
					// cout << count << endl;
				}
			}
		}

		printf("Case #%d: %d\n",i,count);
	}

	return 0;
}