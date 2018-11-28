#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <stack>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
unsigned long long one = 1;

int t,n,a,b,c,d;
double naomi[1010], ken[1010];

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d",&n);
		for (int i=0; i<n; i++){
			scanf("%lf",&naomi[i]);
		}
		for (int i=0; i<n; i++){
			scanf("%lf",&ken[i]);
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		c = 0;
		a = 0;
		b = 0;
		while (a < n && b < n){
			if (naomi[a] > ken[b]){
				c++;
				a++;
				b++;
			} else a++;
		}
		d = n;
		a = 0;
		b = 0;
		while (a < n && b < n){
			if (ken[a] > naomi[b]){
				d--;
				a++;
				b++;
			} else a++;
		}
		printf("Case #%d: %d %d\n",jj,c,d);
	}
	return 0;
}
