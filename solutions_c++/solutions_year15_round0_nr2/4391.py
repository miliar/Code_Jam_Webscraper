#include<stdio.h>
#include<algorithm>
#include<map>
#include<list>
#include<queue>
#include <iostream>
#include<memory.h>
#define MAXN 500050
using namespace std;

typedef long long ll;
int c[1001];
int f(int curr_max, int min_, int penalty){
    if(curr_max == 1) return min_;
    // split
    int res_min = min_;
    for(int i=1; i<=curr_max/2; ++i){
        int new1 = i;
        int new2 = curr_max-new1;
        int max_curr_count = c[curr_max];
        c[curr_max]= 0;
        c[new1]+=max_curr_count;
        c[new2]+= max_curr_count;
        int new_max = curr_max;
        while(c[new_max]==0){
            new_max--;
        }
        int new_min = min(min_, new_max + penalty+ max_curr_count);
        res_min = min(res_min, new_min);
        res_min = min(res_min, f(new_max, new_min, penalty+max_curr_count));
        c[curr_max]= max_curr_count;
        c[new1]-= max_curr_count;
        c[new2]-= max_curr_count;
    }

    return res_min;

}
int main(){
    ios_base::sync_with_stdio(false);

    //freopen("C:\\in.txt", "r", stdin);
   // freopen("C:\\gcj2015\\B_small.in", "r", stdin);
  //  freopen("C:\\gcj2015\\B_small_brute.out", "w", stdout);
    int TC;
    int n,x;
    cin >> TC;
    for(int test_case = 1; test_case<=TC; ++test_case){
        memset(c, 0 , sizeof(c));
        cin >> n;
        int max_x = -1;
        while(n--){
            cin >> x;
            c[x]++;
            max_x = max(max_x, x);
        }
        int min_ = max_x;

            min_ = f(max_x, min_, 0);

        cout << "Case #" << test_case << ": " << min_ << "\n";
    }
    return 0;
}
