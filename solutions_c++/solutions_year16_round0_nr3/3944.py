#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;
int t, cases, N, J;
typedef long long LL;
LL d[15];
int dd[18];
string convertToBaseStr(int n){
    memset(dd, 0, sizeof dd);
    int lastOne = 0;
    for(int i = 0; i < N; ++i){
        if(1 &(n >> i)){
            dd[i] = 1;
            lastOne = i;
        }
    }
    string str;
    for(int i = lastOne; i >= 0; --i){
        str.push_back(dd[i] + '0'); 
    }
    return str;
}
LL convertToBase(int n, int b){
    LL bb = 1;
    LL ret = 0;
    string str = convertToBaseStr(n);
    for(int i = str.size() - 1; i >= 0; --i){
        int d = str[i] - '0';
        if(d)ret = ret + bb * d;
        bb *= b;
    }
    return ret;
}
int produce(int n){
    if(!(1 & n) )return false;
    memset(d, 0, sizeof d);
    for(int i = 2; i <= 10; ++i){
        LL num = convertToBase(n, i);
        for(LL j = 2; j * j <= num; ++j)if(num % j == 0){
            d[i] = j;
            break;
        }
    }
    for(int i = 2; i <= 10; ++i)if(d[i] == 0)return false;
    return true;
}
vector< vector<LL> >v;
vector<string>vs;
int main(){
    freopen("c_small.in", "r", stdin);
    freopen("c_small.out", "w", stdout);
    scanf("%d", &t);
    while(t--){
        v.clear();
        scanf("%d %d", &N, &J);
        int total = 0;
        for(int i = (1 << (N - 1)); i < (1 << N); ++i){
            if(produce(i)){
                vector<LL>vv;
                string str = convertToBaseStr(i);
                vs.push_back(str);
                for(int j = 2; j <= 10; ++j)vv.push_back(d[j]);
                v.push_back(vv);
                total++;
                if(total == J)break;
            }
        }
        printf("Case #%d:\n", ++cases);
        for(int i = 0; i < v.size(); ++i){
            cout << vs[i];
            for(int j = 0; j < v[i].size(); ++j){
                printf(" ");
                printf("%lld", v[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
