#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<limits>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second
#define PP system("PAUSE");

using namespace std;

vector<long long int> fsnum;

bool palin(long long int num){
    long long int tmp = num;
    long long int tmp1 = 0;
    while(tmp){
        tmp1 = tmp1*10+(tmp%10);
        tmp /= 10;
    }
    if(tmp1 == num) return true;
    return false;
}

void init(void){
    for(long long int i = 1; i < 10000000; i++){
        if(!palin(i) || !palin(i*i)) continue;
        fsnum.PB(i*i);
    }
    return;
}

int main(void){
    init();
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        long long int A, B;
        scanf("%I64d%I64d", &A, &B);
        printf("%d\n", upper_bound(fsnum.begin(), fsnum.end(), B)-lower_bound(fsnum.begin(), fsnum.end(), A));
    }
    return 0;
    }
