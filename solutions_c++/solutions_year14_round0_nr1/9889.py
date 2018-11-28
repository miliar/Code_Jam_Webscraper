#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
const int MOD =1e9 + 7;
const int INF = 0x3f3f3f3f;

const int MXN=1e6;
int N,M;

int A[20];
int B[20];
int Ans[20];
void Fun(){
    memset(Ans,0,sizeof(Ans));
    for(int i=0;i<4;++i){
        Ans[A[4*(N-1)+i]]++;
        Ans[B[4*(M-1)+i]]++;
    }
    vector<int> ret;
    for(int i=1;i<=16;++i){
        if(Ans[i]==2)
            ret.push_back(i);
    }
    if(ret.size()==1) printf("%d\n",ret[0]);
    if(ret.size()==0) puts("Volunteer cheated!");
    if(ret.size()>=2) puts("Bad magician!");

}
void Rush()
{
    int T;
    scanf("%d",&T);
    for(int kas=1;kas<=T;++kas)
    {
        printf("Case #%d: ",kas);
        scanf("%d",&N);
        for(int i=0;i<16;++i) scanf("%d",&A[i]);
        scanf("%d",&M);
        for(int i=0;i<16;++i) scanf("%d",&B[i]);
        Fun();
    }
}
int main() 
{
    freopen("out.txt","w",stdout);
    Rush();
    return 0;
}
