#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<map>
#include<set>

using namespace std;

#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define INF 2100000000
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

int main(){
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int tc,ans,tmp;
    vi v,v2;
    scanf("%d",&tc);
    REP(t,1,tc){
        printf("Case #%d: ", t);
        scanf("%d",&ans);
        REP(i,0,3){
            REP(j,0,3){
                scanf("%d",&tmp);
                if(i==ans-1)
                    v.push_back(tmp);
            }
        }
        scanf("%d",&ans);
        REP(i,0,3){
            REP(j,0,3){
                scanf("%d",&tmp);
                if(i==ans-1)
                    v2.push_back(tmp);
            }
        }
        int same = 0;
        int ans = -1;
        REP(i,0,3)
            REP(j,0,3)
                if(v[i]==v2[j]){
                    same++;
                    ans=v[i];
                }
        if(same==1)
            printf("%d\n",ans);
        else if(same==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
        v.clear();
        v2.clear();
    }
    return 0;
}
