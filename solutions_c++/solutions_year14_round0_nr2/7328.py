/*
ID: happine2
LANG: C++
TASK: 
*/

/* 2^31 = 2 147 483 648 (10)
 * 2^32 = 4 294 967 296 (10)
 * 2^64 = 18 446 744 073 709 551 616 (20) */


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

#define DATA_SIZE 17
#define MAX_TIME 1000000000.0
int main() {
	int i, j;
	int cas = 0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    double c, f, x;
    scanf("%d", &t);
    while(t--) {
		double cur_sum, per_sum;
		cur_sum = per_sum = 0.00000;

		scanf("%lf %lf %lf", &c, &f, &x);
		per_sum = x / 2.0;
		cur_sum = per_sum;
	    int cnt = 1;
		double speed;
		while(per_sum > cur_sum || cnt == 1) {
			per_sum = cur_sum;
			speed = 2.0000;
			cur_sum = 0.00000;
			for (i = 0 ; i < cnt ; ++i) {
				cur_sum += c / speed;
				speed += f;
			}
			cur_sum += x / speed;
			cnt++;
			
		}
		cas++;
        printf("Case #%d: %.7lf\n", cas, per_sum);
    }
    return 0;
}
