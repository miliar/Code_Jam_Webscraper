#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <memory.h>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef pair<int, int> ii;
typedef pair<double, ii> edge;

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T, cnum = 1;
    cin >> T;
    while(T--){
        int N;
        string d;
        cin >> N >> d;

        int invite = 0, seen = d[0] - '0';
        for(int i = 1; i <= N; i++){
            int shy = i, p = d[i] - '0';
            if(p == 0) continue;
            if(shy > seen){
                invite += shy - seen;
                p += shy - seen;
            }
            seen += p;
        }
        printf("Case #%d: %d\n", cnum, invite);
        cnum++;
    }
}
