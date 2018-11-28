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
const int L = 1000;
char s[L];
int answer;

int solve(char s[]) {
    int l = strlen(s);
    char c = s[0];
    answer = 0;
    for(int i = 0 ; i <  l ; ++i) {
        if(s[i] != c)++answer;
        c = s[i];
    }
    if(c == '-')++answer;
    return answer;
}


void print() {
    printf("Case #%d: ", cases);
    printf("%d",answer);
    printf("\n");
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(cases = 1 ; cases <= T ; ++cases) {
        scanf("%s",s);
        solve(s);
        print();
    }
}

