#include <bits/stdc++.h>
using namespace std;

#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

#define M(x) (((x%MOD)+MOD)%MOD)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const ll MOD = (ll)(1e9)+7ll;

string req[15][3];
int num[15][3][3];
string o = "PRS";

int get(char c) {
    for(int i=0;i<3;i++) {
        if(c == o[i]) {
            return i;
        }
    }
    return -1;
}

int main() {
    for(int i=0;i<3;i++) {
        req[0][i] += o[i];
        for(auto c: req[0][i]) {
            num[0][i][get(c)]++;
        }
    }

    for(int i=1;i<15;i++) {
        for(int j=0;j<3;j++) {
            string a = req[i-1][j];
            string b = req[i-1][(j+1)%3];
            if(a > b) {
                swap(a, b);
            }
            req[i][j] = a+b;
            for(auto c: req[i][j]) {
                num[i][j][get(c)]++;
            }
    //        D("req[%d][%d] = %s\n",i,j,req[i][j].c_str());
            for(int k=0;k<3;k++) {
     //           D("num[%d][%d][%d] = %d\n",i,j,k,num[i][j][k]);
            }
        }
    }

    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        printf("Case #%d: ",z);

        int N;
        int nums[3];
        scanf("%d",&N);
        scanf("%d %d %d",&nums[1],&nums[0],&nums[2]);

        int nn = N;

        string can = "";
        for(int i=0;i<3;i++) {
            bool ok =true;
            for(int j=0;j<3;j++) {
                if(num[nn][i][j] != nums[j]) {
                    ok = false;
                    break;
                }
            }
            if(ok) {
                if(can.empty() || can > req[nn][i]) {
                    can = req[nn][i];
                }
            }
        }
        if(!can.empty()) {
            printf("%s\n",can.c_str());
        } else {
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;
}
