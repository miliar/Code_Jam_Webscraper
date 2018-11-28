#include <iostream>
#include <sstream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
#define Si size()
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;

vector <long long> list;

void prework(){
    list.pb(1);
    list.pb(4);
    list.pb(9);
    list.pb(121);
    list.pb(484);
    list.pb(10201);
    list.pb(12321);
    list.pb(14641);
    list.pb(40804);
    list.pb(44944);
    list.pb(1002001);
    list.pb(1234321);
    list.pb(4008004);
    list.pb(100020001);
    list.pb(102030201);
    list.pb(104060401);
    list.pb(121242121);
    list.pb(123454321);
    list.pb(125686521);
    list.pb(400080004);
    list.pb(404090404);
    list.pb(10000200001);
    list.pb(10221412201);
    list.pb(12102420121);
    list.pb(12345654321);
    list.pb(40000800004);
    list.pb(1000002000001);
    list.pb(1002003002001);
    list.pb(1004006004001);
    list.pb(1020304030201);
    list.pb(1022325232201);
    list.pb(1024348434201);
    list.pb(1210024200121);
    list.pb(1212225222121);
    list.pb(1214428244121);
    list.pb(1232346432321);
    list.pb(1234567654321);
    list.pb(4000008000004);
    list.pb(4004009004004);
}


int main(){
    long long A,B;
    freopen("cc.in","r",stdin);
    freopen("cc.out","w",stdout);
    int T;
    prework();
    scanf("%d",&T);
    for (int i=1;i<=T;++i){
        printf("Case #%d: ",i);
        cin>>A>>B;
        int ans=0;
        for (int i=0;i<list.Si;++i)
            if (list[i]>=A && list[i]<=B) ans++;
        cout<<ans<<endl;
    }
    return 0;
}
