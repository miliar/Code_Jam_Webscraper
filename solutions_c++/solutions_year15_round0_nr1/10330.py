#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MP make_pair
#define PB push_back
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

typedef long long LL;
typedef long double LD;
int shy;
int req;
int tot;
int fri;
char aa;
void solve(int test)
{
    fri=0;
    tot=0;
    req=0;
    printf("Case #%d: ", test);
    scanf("%d",&shy);
    scanf("%c",&aa);
    for(int i=0;i<=shy;i++){
        char p;
        scanf("%c",&p);
        req=i;
        if(tot<req){
            fri=fri+req-tot;
            tot=tot+req-tot;
        }
        
        tot=tot+(p-48);
        
        
    }
   printf("%d\n",fri);

    
    
}

int main()
{
    //freopen("A.in", "r", stdin); freopen("A.out", "w", stdout);
    //freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in.txt", "r", stdin); freopen("A-large.out.txt", "w", stdout);
    int testcase;
    scanf("%d", &testcase);
    for(int i = 1; i <= testcase; ++ i) solve(i);
    fclose(stdout);
    return 0;
}
