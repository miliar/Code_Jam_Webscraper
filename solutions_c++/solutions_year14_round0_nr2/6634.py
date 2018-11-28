#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define sz(X) ((int)(X.size()))
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
#define up(i,s,e) for(int i=s;i<e;i++)
#define down(i,s,e) for(int i=s;i>e;i--)
#define INF 0x7FFFFFFF

int main(){
    
    #ifndef ONLINE_JUDGE
    	freopen("/Users/maoweiye/Desktop/c++/program/program/input.txt", "r", stdin);
    #endif
    int t;
    scanf("%d",&t);

    up(i,1,t+1){
        double c,f,x,res=0;
        scanf("%lf %lf %lf",&c,&f,&x);
        double produce = 2.0;
        while(1){
            double notBuy = x/produce;
            double buy = c/produce + x/(f+produce);
            if(notBuy <= buy){
                res += notBuy;
                break;
            }else{
                res += c/produce;
                produce += f;
            }
        }
        
        printf("Case #%d: %.7lf\n",i,res);
    }
    
    return 0;
}












