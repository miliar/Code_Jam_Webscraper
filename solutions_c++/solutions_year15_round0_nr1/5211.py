#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-13
#define INF 0x3f3f3f3f
#define LL long long

using namespace std;

int now,ned,T,s;
char str[1001];

int main(){
    ifstream cins("A-large.in");
    ofstream couts("A-large.out");
    cins>>T;
    //scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        //scanf("%d %s",&s,str);
        cins>>s>>str;
        now=ned=0;
        for(int i=0;i<=s;i++)if(str[i]!='0'){
            if(now<i){
                ned+=i-now;
                now=i;
            }
            now+=str[i]-'0';
        }
        couts<<"Case #"<<cas<<": "<<ned<<endl;
        //printf("Case #%d: %d\n",cas,ned);
    }
    return 0;
}
/*

4
4 11111
1 09
5 110011
0 1


*/

