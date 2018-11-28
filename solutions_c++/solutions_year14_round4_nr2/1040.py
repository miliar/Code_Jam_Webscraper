#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long

using namespace std;

const int SIZ = 1000;
typedef vector<int> VI;

int seq[SIZ + 2], max_e= 0, N, max_pos;
vector<int>S;

int inv_counting(int L, int R) {

    if( R <= L) {
        return 0;
    }
    int ret = 0;
    VI temp;
    for(int i = L; i <= R; i++) {
        temp.push_back(S[i]);
    }
    for(int i = 0; i < temp.size() - 1; i++) {
        if(temp[i] > temp[i + 1]) {
            swap(temp[i], temp[i + 1]);
            ret ++;
            i = -1;
        }
    }

    return ret;
}

int rev_inv_counting(int L, int R) {

    if( R <= L) {
        return 0;
    }


    VI temp;
    int ret = 0;

    for(int i = L; i <= R; i++) {
        temp.push_back(S[i]);
        //cerr << temp.back() << endl;
    }
    for(int i = 0; i < temp.size() - 1; i++) {
        if(temp[i] < temp[i + 1]) {
            swap(temp[i], temp[i + 1]);
            ret ++;
            i = -1;
        }
    }


    //cerr << L << " " << R <<  " " << ret << endl;
    return ret;
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    cin >> T;

    for(int cas = 1; cas <= T; cas ++) {
        cin >> N;

        int ret = 0;
        max_pos = 0;
        max_e = 0;

        for(int i = 0; i < N; i++) {
            cin >> seq[i];
            if(max_e < seq[i]) {
                max_pos = i;
            }
            max_e = max(max_e, seq[i]);
        }

        for(int i = 0; i < N; i++) {

            int l = 0, r = 0;

            for(int j = 0; j < i ; j++) {
                //cerr << j << " " << seq[j] << " " << seq[i] << endl;
                if(seq[j] > seq[i]) {
                    l ++;
                }
            }
            for(int j = i + 1; j < N; j++) {
                if(seq[j] > seq[i]) {
                    r ++;
                }
            }
            //cerr << l << " " << r << endl;
            ret += min(l, r);
            //seq[i] = -1;
        }

        printf("Case #%d: %d\n", cas, ret);
    }

}
