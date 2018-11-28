#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <utility>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

#define For(i,a,b) for(typeof(a) i =(a);i<(b);i++)
#define ll long long
#define pb push_back
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(V) V.begin(),V.end()
/*****************************************************************************/

int t,r1,r2;
vector<int> temp1,temp2,ret;
int main(){
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        scanf("%d",&r1);
        For(i,0,4){
            vector<int> cur(4);
            For(j,0,4) scanf("%d",&cur[j]);
            if (i+1==r1) temp1 = cur;
        }
        scanf("%d",&r2);
        For(i,0,4){
            vector<int> cur(4);
            For(j,0,4) scanf("%d",&cur[j]);
            if (i+1==r2) temp2 = cur;
        }
        sort(ALL(temp1));
        sort(ALL(temp2));
        vector<int> ret;
        For(i,0,temp1.size()) For(j,0,temp2.size()){
            if (temp1[i]==temp2[j]) ret.pb(temp1[i]);
        }
        printf("Case #%d: ",cas);
        if (ret.size()==1){
            printf("%d\n",ret[0]);
        }
        if (ret.size()>1){
            printf("Bad magician!\n");
        }
        if (ret.size()==0){
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
