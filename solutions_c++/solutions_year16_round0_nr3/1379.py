//#####################
//Author:fraud
//Blog: http://www.cnblogs.com/fraud/
//#####################
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <sstream>
#include <ios>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
using namespace std;
#define XINF INT_MAX
#define INF 0x3FFFFFFF
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define rep(X,N) for(int X=0;X<N;X++)
#define rep2(X,L,R) for(int X=L;X<=R;X++)
#define dep(X,R,L) for(int X=R;X>=L;X--)
#define clr(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define ALL(X) (X).begin(),(X).end()
#define PQ std::priority_queue
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;


int main(){
    ios::sync_with_stdio(0);
    int t;
    int cas = 1;
    freopen("Cl.in","r",stdin);
    freopen("Cl.out","w",stdout);
    cin >> t;
    while(t--){
        int n,m;
        cin >> n >> m;
        int tot = 511;
        cout << "Case #" << cas ++ << ":" << endl;
        int len = (n - 4) / 2;
        tot = 1 << len;
        int now = 0;
        while(m--){
            //string ans = "";
            string str = "11";
            rep(i,len){
                if(now & (1 << i))str = str + "11";
                else str = str + "00";
            }
            str += "11";
            cout << str;
            for(int i = 2; i <= 10;i++){
                cout << " " << i + 1;
            }
            cout << endl;
            now ++;
        }
    }

}

