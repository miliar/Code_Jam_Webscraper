//Template of CyberKasumi (Jennifer Santoso a.k.a. Liang Qiuxia)

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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
using namespace std;

#define LL long long
#define inf 2123123123
#define MOD 1000000007

int tcase;
int r1,r2;
int first[6][6];
int second[6][6];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    scanf("%d",&tcase);
    for (int i=1;i<=tcase;i++){
        scanf("%d",&r1);
        for (int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                scanf("%d",&first[j][k]);
            }
        }
        scanf("%d",&r2);
        for (int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                scanf("%d",&second[j][k]);
            }
        }
        r1--,r2--;
        int coun=0;
        int num=0;
        for (int j=0;j<4 && coun<=1;j++){
            for (int k=0;k<4 && coun<=1;k++){
                if (first[r1][j]==second[r2][k]){
                    coun++;
                    num=first[r1][j];
                }
            }
        }
        printf("Case #%d: ",i);
        if (coun>1)printf("Bad magician!\n");
        else if (coun==1)printf("%d\n",num);
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
