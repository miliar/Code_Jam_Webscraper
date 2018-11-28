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

#define SIZE 20

int cnt[SIZE];
int arr[10][10];

int main(){

    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);

    int kase;
    scanf("%d",&kase);

    for ( int kk=1; kase-- ;++kk ){
        int q;
        CLR(cnt);

        scanf("%d",&q);

        for (int i=0;i<4;++i){
            for (int j=0;j<4;++j){
                scanf("%d",&arr[i][j]);
                if ( i+1 == q ){
                    cnt[ arr[i][j] ]++;
                }
            }
        }

        scanf("%d",&q);
        for (int i=0;i<4;++i){
            for (int j=0;j<4;++j){
                scanf("%d",&arr[i][j]);
                if ( i+1 == q ){
                    cnt[ arr[i][j] ]++;
                }
            }
        }

        int found2=0,ans=-1;
        for (int i=0;i<SIZE;++i){
            if ( cnt[ i ] == 2 ){
                found2++;
                ans = i;
            }
        }
        printf("Case #%d: ",kk);
        if ( found2==1 ){
            printf("%d\n",ans);
        }else if ( found2==0 ){
            printf("Volunteer cheated!\n");
        }else{
            printf("Bad magician!\n");
        }
    }

    return 0;
}
