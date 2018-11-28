#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
using namespace std;


int main() {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while (T--){
        int a,b;
        scanf("%d",&a);
        set<int>s;
        for (int i=1;i<=4;i++){
            for (int j=1;j<=4;j++){
                int num;
                scanf("%d",&num);
                if (i==a){
                    s.insert(num);
                }
            }
        }
        scanf("%d",&a);
        int cnt=0,ans=-1;
        for (int i=1;i<=4;i++){
            for (int j=1;j<=4;j++){
                int num;
                scanf("%d",&num);
                if (i==a){
                    if (s.count(num)){
                        ans=num;
                        cnt++;
                    }
                }
            }
        }
        printf("Case #%d: ",cas++);
        if (cnt==1){
            printf("%d\n",ans);
        }
        else if (cnt==0){
            puts("Volunteer cheated!");
        }
        else {
            puts("Bad magician!");
        }
    }
    return 0;
}
