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

    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for( int kk=1;kase--;++kk){
        double have =0;
        double pro=2;
        double target,c,f;
        scanf("%lf %lf %lf",&c,&f,&target);

        double ans = 0;
        while ( true ){
            if ( target/pro < c/pro + target/( pro+f )  ){
                ans+= target/pro;
                break;
            }else{
                ans+= c/pro;
                pro+=f;
            }
        }
        printf("Case #%d: %.7lf\n",kk,ans);
    }


    return 0;
}
