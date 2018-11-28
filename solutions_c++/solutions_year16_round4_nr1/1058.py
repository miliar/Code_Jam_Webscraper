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
#include <cstring>
using namespace std;
struct node{
    int a,b,c;
    string num;
    node(){
        a=b=c=0;
        num="";
    }
}A[12][3];
int B[3][2]={
    {0,2},
    {1,0},
    {2,1},
};
node operator + (node x,node y){
    node ans;
    ans.a=x.a+y.a;
    ans.b=x.b+y.b;
    ans.c=x.c+y.c;
    ans.num=x.num+y.num;
    return ans;
}
int n,a,b,c;
int suma,sumb,sumc;
string ans;
string now;
char s[]={'R','P','S'};
int main(){
    freopen("in.in","r",stdin);
    freopen("check.out","w",stdout);
    A[0][0].a=1;A[0][0].num='R';
    A[0][1].b=1;A[0][1].num='P';
    A[0][2].c=1;A[0][2].num='S';
    for(int j=1;j<=12;j++){
        for(int k=0;k<=2;k++){
            node a=A[j-1][B[k][0]],b=A[j-1][B[k][1]];
            if(a.num<b.num) A[j][k]=a+b;
            else A[j][k]=b+a;
        }
    }
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d%d",&n,&a,&b,&c);
        ans="";
        for(int j=0;j<=2;j++){
            //printf("a = %d b= %d c = %d\n",A[n][j].a,A[n][j].b,A[n][j].c);
            if(a==A[n][j].a&&b==A[n][j].b&&c==A[n][j].c){
                if(ans=="") ans=A[n][j].num;
                else ans=min(ans,A[n][j].num);
            }
        }
        printf("Case #%d: ",cas++);
        if(ans=="") printf("IMPOSSIBLE\n");
        else cout<<ans<<endl;
    }
    return 0;
}
