#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <random>

using namespace std;

typedef long long ll;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define tget(X,id) get<id>(X)

#define MAXN 1005

string FILE_IN, FILE_OUT;

char S[1005];

int main(int argc, char *argv[]){
    if (argc == 1){
        cerr<<"No input specified, using A.in"<<endl;
        FILE_IN = "A.in";
        FILE_OUT = "A.out";
    } else {
        FILE_IN = string(argv[1]);
        FILE_OUT = FILE_IN + ".out";
    }
    freopen(FILE_IN.c_str(),"r",stdin);
    freopen(FILE_OUT.c_str(),"w",stdout);
    
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++){
        int K, len;
        scanf("%s%d", S, &K);
        len = strlen(S);
        int ans = 0;
        for (int i = 0; i < len-K+1; i++){
            if (S[i] == '-'){
                ans++;
                for (int j = 0; j < K; j++)
                    if (S[i+j] == '-')
                        S[i+j] = '+';
                    else
                        S[i+j] = '-';
            }
        }
        for (int i = 1; i < K; i++)
            if (S[len-K+i] == '-')
                ans = -1;
        printf("Case #%d: ", _t);
        if (ans == -1)
            printf("IMPOSSIBLE");
        else
            printf("%d", ans);
        printf("\n");
    }
    return 0;
}
