#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <limits.h>
#include <math.h>
#include <iomanip>
#include <bitset>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long LL;
typedef pair<int,int> pii;
int n,T,cases;
bool shown[10];
int answer;
const int C = 1000;

long long solve(long long base) {
    if(base == 0)return answer = C+1;
    answer = 0;
    memset(shown,0,sizeof(shown));
    int left = 10;
    while(answer <= C) {
        ++answer;
        long long tmp = base*answer;
        for(;tmp;tmp/=10) {
            if(!shown[tmp%10])--left;
            shown[tmp%10] = true;
        }
        if(left==0)return answer;
    }
}

void print() {
    printf("Case #%d: ", cases);
    if(answer > C) {
        printf("INSOMNIA");
    } else {
        printf("%I64d",(long long)answer*n);
    }
    printf("\n");
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(cases = 1 ; cases <= T ; ++cases) {
        scanf("%d",&n);
        solve(n);
        print();
    }
}
