/* @coder: Sidharth Gupta */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
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


#define MOD 109546051211ll
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

int main() {

    int t, T, n;
    int arr[1005][30];
    int arr1[30][2];

    scanf("%d",&T);

    for(t=1;t<=T;++t) {
        SET(arr, 0);
        SET(arr1, 0);

        scanf("%d", &n);
        for(int i=0;i<n;++i) {
            int x;
            scanf("%d", &x);
            arr[x][i] = 1;
        }

        int x = 0;
        for(int i=0;i<=1000;++i) {
            for(int j=0;j<=25;++j) {
                if(arr[i][j]) {
                    arr1[x][1] = i;
                    arr1[x][0] = 'A' + j;
                    ++x;
                }
            }
        }

        printf("Case #%d:",t);
        int mn = arr1[0][1];
//        for(int i=x-1;i>0;--i) {
//            for(int j=arr1[i][1]; j > mn; --j) {
//                printf(" %c",arr1[i][0]);
//            }
//            //system("pause");
//            arr1[i][1] = mn;
//        }

        for(int j=mn+1;j<=arr1[x-1][1];++j) {
            for(int i=x-1;i>=0;--i) {
                if(arr1[i][1]>=j) {
                    printf(" %c",arr1[i][0]);
                }
            }
        }

        //system("pause");

        for(int i=mn;i>0;--i) {
            for(int j=0;j<x-2;++j) {
                printf(" %c", arr1[j][0]);
            }
        }

        for(int i=mn;i>0;--i) {
            for(int j=x-2;j<x-1;++j) {
                printf(" %c%c", arr1[j][0],arr1[j+1][0]);
            }
        }

        if(t!=T) printf("\n");
    }

    return 0;
}
