//============================================================================//
//------------------------>Nguyen Quoc Nhan<----------------------------------//
//--------------------->quocnhan1843@gmail.com<-------------------------------//
//============================================================================//


#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i=0; i<n; i++)
#define fr(i,a,b) for(int i=a; i<=b; i++)
#define debug(a) cout<< #a << " = " <<a<<endl;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back

#define oo 2147483647
#define INF 12512523232344LL
#define pi 3.1415926535897932
#define MaxN 1000000

int GCD(int a, int b){return(b==0?a:GCD(b,a%b));}
int LCM(int a, int b){return a*(b/GCD(a,b));}

int T, smax, current, res;
string str;

int main(){


    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);


    cin >> T;

    fr(testCase,1,T){
        cin >> smax >> str;

        current = 0;
        res = 0;

        for(int i=0; i<=smax; i++){
            int num = str[i] - '0';
            int need = i;

            if(num == 0) continue;

            if(current < need){ res += need - current; current += need -current;}

            current += num;
        }

        cout << "Case #" << testCase << ": " <<  res << endl;
    }


return 0;
}
