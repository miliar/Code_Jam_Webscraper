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
int visited[DATA_SIZE];


int main() {
	int i, j;
	int cas = 0;
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    int t;
    int row1, row2;
    scanf("%d", &t);
    while(t--) {
       scanf("%d", &row1);
       int tmp;
       set_zero(visited);
       for ( i = 0 ; i < 4 ; ++i) {
         for ( j = 0 ; j < 4 ; ++j) {
           scanf("%d", &tmp);
           if (row1 == i + 1) {
             visited[tmp]++;
           }
         }
       }
       scanf("%d", &row2);
       for ( i = 0 ; i < 4 ; ++i) {
         for ( j = 0 ; j < 4 ; ++j) {
           scanf("%d", &tmp);
           if (row2 == i + 1) {
             visited[tmp]++;
           }
         }
       }
       int cnt2 = 0;
       int sit = 0;
       for ( i = 1 ; i <= 16 ; ++i) {
         if (visited[i] >= 2) {
           cnt2++;
           sit = i;
         }
       }
	   cas++;
       if (cnt2 <= 0) {
        printf("Case #%d: Volunteer cheated!\n", cas);
       } else if (cnt2 == 1) {
         printf("Case #%d: %d\n", cas, sit);
       } else if (cnt2 > 1) {
		    printf("Case #%d: Bad magician!\n", cas);
		 
       }
    }
    return 0;
}
