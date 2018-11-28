#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <string>
#include <functional>
#include <utility>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

void print_vector(vi v);
void print_array(int* array, int start, int end);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i > _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc, cse=1;
double c, f, x;
int k;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    s(tc);
    while(tc--){
        sf(c), sf(f), sf(x);
        k = 0;
        double prevans = 1000000000, currans = 0;
        double ans1, ans2, ans3;
        int begin = 0, end = 100001;

        while(begin < end){
          //printf("%d %d\n", begin, end);
            int mid = (begin + end)/2;
            if(mid == 0){
                k = mid;
                ans2 = 0;
                FOR(i, 1, k+1){
                    ans2 += c / (2.0 + (i-1) * f);
                }
                ans2 += x / (2.0 + k * f);

                k = mid+1;
                ans3 = 0;
                FOR(i, 1, k+1){
                    ans3 += c / (2.0 + (i-1) * f);
                }
                ans3 += x / (2.0 + k * f);
                if(ans2 < ans3) end = mid;
                else begin = mid+1;
                break;
            }

            k = mid-1;
            ans1 = 0;
            FOR(i, 1, k+1){
                ans1 += c / (2.0 + (i-1) * f);
            }
            ans1 += x / (2.0 + k * f);

            k = mid;
            ans2 = 0;
            FOR(i, 1, k+1){
                ans2 += c / (2.0 + (i-1) * f);
            }
            ans2 += x / (2.0 + k * f);

            k = mid+1;
            ans3 = 0;
            FOR(i, 1, k+1){
                ans3 += c / (2.0 + (i-1) * f);
            }
            ans3 += x / (2.0 + k * f);
           // printf("%lf %lf %lf\n", ans1, ans2, ans3);
            if(ans1 > ans2 && ans2 > ans3) {
                begin = mid+1;
            } else if (ans1 < ans2 && ans2 < ans3) {
                end = mid-1;
            } else {
                begin = mid; break;
            }
        }
        k = begin;
        ans1 = 0;
        FOR(i, 1, k+1){
            ans1 += c / (2.0 + (i-1) * f);
        }
        ans1 += x / (2.0 + k * f);
        printf("Case #%d: %.7lf\n", cse++, ans1);
        
        // while(true){
        //     currans = 0;
        //     FOR(i, 1, k+1){
        //         currans += c / (2.0 + ((double)i-1.0) * f);
        //     }
        //     currans += x / (2.0 + k * f);
        //     if(currans < prevans) prevans = currans;
        //     else break;
        //     k++;
        // }
        // printf("Case #%d: %.7lf\n", cse++, prevans);
    }
    return 0;
}

void print_array(int* array, int start, int end){
  printf("[");
  FOR(i, start, end){
    printf("%d ", array[i]);
  }
  printf("]");
  printf("\n");
}

void print_vector(vi v){
  printf("[");
  FOR(i, 0, v.size()){
    printf("%d ", v[i]);
  }
  printf("]");
  printf("\n");
}