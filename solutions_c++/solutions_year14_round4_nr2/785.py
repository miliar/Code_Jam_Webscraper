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
int a[1010];

int main(){
freopen("B.in","r",stdin);
freopen("B.out","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1; tc <= TC; tc++){
		cin >> n;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		int l = 0;
		int r = n - 1;
		int res = 0;
		for(int i = 0; i < n; i++){
			///busco el menor
			int s = l;
			for(int j = l; j <= r; j++)
				if(a[j] < a[s])
					s = j;
			///muevo el menor.
			if(s - l < r - s){///mover a la izquierda
				res += (s - l);
				int tmp = a[s];
				for(int j = s - 1; j >= l; j--){
					a[j + 1] = a[j];
				}
				a[l] = tmp;
				l++;
			}
			else{///mover a la derecha
				res += (r - s);
				int tmp = a[s];
				for(int j = s; j <= r - 1; j++){
					a[j] = a[j + 1];
				}
				a[r] = tmp;
				r--;
			}
		}
		cout << "Case #" << tc << ": " << res << endl;
	}
    return 0;
}
