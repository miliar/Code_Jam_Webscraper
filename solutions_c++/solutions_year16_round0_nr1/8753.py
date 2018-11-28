/*
Bismillahir Rahmanir Rahim
Coder: Ahmad Faiyaz
*/

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <fstream>
#include <ctime>


# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)

#define EPS 1e-11
#define inf 1234567891
#define LL long long

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))

#define pb push_back
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define pii pair<int,int>
#define UNIQUE(c) (c).resize( unique( all(c) ) - (c).begin() )

#define READ(f) {ifstream infile(f) ;if(infile.good()) freopen(f, "r", stdin);}
#define WRITE(f) freopen(f, "w", stdout)
#define CIN ios_base::sync_with_stdio(0);
///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;
#include <unordered_map>

unordered_map <long long int, int> st;

int getMask(long long int x){
    if(st.find(x) != st.end()){
        return st[x];
    }

    if(x == 0){
        return 1;
    }

    int ret = 0;
    while(x){
        int dig = x%10;

        ret |= (1<<dig);

        x/= 10;
    }

    return st[x] = ret;
}

int main(){
    #if defined( faiyaz_pc )
        READ("A-large.in");
        WRITE("big.txt");
    #endif // defined


    int t = 1000000, chk = 1;
    LL n = 1000001;


    scanf("%d", &t);

    while(t--){
        scanf("%lld", &n);
        printf("Case #%d: ", chk++);
        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }

        int msk = 0;

        int lim = (1<<10) - 1;



        for(long long int i=1;;i++){
            long long int mul = i * n;

            msk |= getMask(mul);

            if(msk == lim){
                printf("%lld\n", mul);
                break;
            }
        }

    }

    return 0;
}
