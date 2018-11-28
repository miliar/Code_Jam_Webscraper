///SACAR FREOPEN.
#include <iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<list>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<map>
#include<sstream>
#include<assert.h>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define forn(i,n) for(int i=0; i<(int)n; i++)
#define dforn(i,n) for(int i=(int)n-1; i>=0; i--)
#define formn(i,m,n) for(int i=m; i<(int)n; i++)
#define dformn(i,m,n) for(int i=n-1; i>=m; i--)
#define mp make_pair
#define pb push_back

const double PI=acos(-1.0);

typedef long long tint;
typedef pair<int,int> pint;

int n;
int x;
int a[10010];

int main(){
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1; tc <= TC; tc++){
		cin >> n >> x;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		sort(a,a + n);
		int lo = 0;
		int hi = n - 1;
		int res = 0;
		while(true){///lo apunta al mas chico sin aparear.
					///hi apunta al mas grande sin aparear.
			if(lo == hi){
				res++;
				break;
			}
			if(lo > hi){
				break;
			}
			if(a[lo] + a[hi] <= x){
				res++;
				lo++;
				hi--;
			}
			else{
				res++;
				hi--;
			}
		}
		cout << "Case #" << tc << ": " << res << endl;
	}
    return 0;
}
