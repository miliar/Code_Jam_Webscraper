#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   ll;

int main() {
    freopen("in_A.txt","r",stdin);
    freopen("out_A.txt","w",stdout);

    int TC,row,m[5][5],cnt,ans;
    bool sw1[20],sw2[20];
    scanf("%d",&TC);
    for(int c=1;c<=TC;c++){
        cnt=0;
        memset(sw1,false,sizeof sw1);
        memset(sw2,false,sizeof sw1);
        scanf("%d",&row);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&m[i][j]);
        for(int j=0;j<4;j++)
            sw1[m[row-1][j]]=true;
        scanf("%d",&row);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&m[i][j]);
        for(int j=0;j<4;j++)
            sw2[m[row-1][j]]=true;
        for(int i=1;i<=16;i++)
            if(sw1[i]&&sw2[i]){
                cnt++;
                ans=i;
            }
        printf("Case #%d: ",c);
        if(cnt==0)printf("Volunteer cheated!\n");
        else if(cnt==1)printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
}
