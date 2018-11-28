#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <climits>

using namespace std;

typedef long long LL;

#define PB push_back
#define FRO freopen("in.txt","r",stdin);

#define CLR(arr) memset( (arr),0,sizeof(arr) );
#define NEG(arr) memset( (arr),-1,sizeof(arr) );

#define X first
#define Y second

#define MP make_pair

#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)


typedef pair<int,int> pint;
typedef map<int,int> mint;

int main(){

    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for (int kk=1;kase--;++kk){
        int a,b,k;
        scanf("%d %d %d",&a,&b,&k);

        int ans = 0;
        for (int i=0;i<a;++i){
            for (int j=0;j<b;++j){
                if ( (i&j) < k){
                    ans++;

                }
                //cout<<i<<" "<<j<<" "<<(i&j)<<endl;
            }
        }
        printf("Case #%d: %d\n",kk,ans);
    }


    return 0;
}
