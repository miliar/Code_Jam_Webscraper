#include <iostream>

#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

using namespace std;

//typedef long long int64;
#define get_max(x, y) ((x)>(y)?(x):(y))
#define get_min(x, y) ((x)<(y)?(x):(y))

#define set_zero(a) (memset(a, 0, sizeof(a)))

#define FLOAT_LIMIT 1e-8
#define feq(a, b) (fabs((a) - (b)) <= FLOAT_LIMIT ? true : false)
template <class type> void do_swap(type &a, type &b) {type t = a; a = b; b = t;}

#define DATA_SIZE 1010
int n;
double naomi[DATA_SIZE];
double ken[DATA_SIZE];
bool visited1[DATA_SIZE];
bool visited2[DATA_SIZE];
int main() {
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
	int t;
	int cas = 0;
	scanf("%d", &t);
    while(t--) {
		scanf("%d", &n);
		set_zero(visited1);
		set_zero(visited2);
		int i;
		for (i = 0 ; i < n ; ++i) {
		    scanf("%lf", &naomi[i]);
		}
		for (i = 0 ; i < n ; ++i) {
		    scanf("%lf", &ken[i]);
		}
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		int cnt1 = 0;
		int cnt2 = 0;
		int j;
		
		for(i = 0 ; i < n; ++i) {
			for (j = 0 ; j < n ; ++j) {
			    if ((naomi[i] < ken[j] || feq(ken[j], naomi[i])) && !visited1[j]) {
					visited1[j] = true;
					cnt2++;
			        break;
				}
			}
			for (j = 0 ; j < n ; ++j) {
			    if (naomi[j] > ken[i] && !visited2[j]) {
					visited2[j] = true;
			        cnt1++;
					break;
				}
			}
		}
		cas++;
		printf("Case #%d: %d %d\n", cas, cnt1, n - cnt2);
	}
    return 0;
}
