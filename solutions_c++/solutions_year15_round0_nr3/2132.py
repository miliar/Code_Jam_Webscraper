#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 100005
typedef long long LL;
typedef unsigned long long ULL;
using namespace std;
int L,X;
char s[10004];
char ac[100000008];
char getNum(char x){
    if( x == '1') return 0;
    if( x == 'i') return 1;
    if( x == 'j') return 2;
    if( x == 'k') return 3;
    
}
char prod[4][4];
char p(char a,char b){
    if( a>=4 ^ b>=4 ){
        return (prod[a%4][b%4]+4)%8;
    }
    return prod[a%4][b%4];
}
char rev(char a,char c){
    FN(i,4){
        if( prod[a%4][i] == c  ){
            if( a>=4 ){
                return i+4;
            }
            return i;
        }
        if( prod[a%4][i] == (c+4)%8 ){
            if( a>=4 ){
                return i;
            }
            return i+4;
        }
    }
}
int main(){
    prod[0][0] = 0;
    prod[0][1] = 1;
    prod[0][2] = 2;
    prod[0][3] = 3;
    
    prod[1][0] = 1;
    prod[1][1] = 4;
    prod[1][2] = 3;
    prod[1][3] = 6;
    
    prod[2][0] = 2;
    prod[2][1] = 7;
    prod[2][2] = 4;
    prod[2][3] = 1;
    
    prod[3][0] = 3;
    prod[3][1] = 2;
    prod[3][2] = 5;
    prod[3][3] = 4;

    int tc;
    sc1(tc);
    FOR(itc,1,tc+1){
        sc2(L,X);  
        scanf("%s",s);
        int ind = 0;
        FN(i,X){
            FN(j,L){
                if(ind != 0) {
                    ac[ind] = p( ac[ind-1] , getNum(s[j]) );
                }else ac[ind] = getNum(s[ind]);                
                ind++;
            }
        }
        bool hay = 0;
        for(int i = 0; i<L*X; i++){
            if( ac[i] == 1){
                for(int j = i+1; j<L*X;j++){
                    if( rev(ac[i],ac[j]) == 2 && rev(ac[j],ac[L*X-1])==3 ){
                        hay = 1;
                        break;
                    }
                }
            }
            if( hay ) break;
        }
        printf("Case #%d: ",itc);
        if( hay ){
            puts("YES");
        }else{
            puts("NO");
        }
    }
}

