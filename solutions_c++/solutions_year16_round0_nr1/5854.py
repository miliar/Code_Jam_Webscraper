/*
*Rainto96
*Beijing University of Posts and Telecommunications School of Software Engineering
*http://blog.csdn.net/u011775691
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <climits>
using namespace std;
#define pb push_back
#define ALL(x) x.begin(),x.end()
#define VINT vector<int>
#define PII pair<int,int>
#define MP(x,y) make_pair((x),(y))
#define ll long long
#define ull unsigned long long
#define MEM0(x)  memset(x,0,sizeof(x))
#define MEM(x,val) memset((x),val,sizeof(x))
#define scan(x) scanf("%d",&(x))
#define scan2(x,y) scanf("%d%d",&(x),&(y))
#define scan3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define scan4(x,y,z,k) scanf("%d%d%d%d",&(x),&(y),&(z),&(k))
#define Max(a,b) a=max(a,b)
#define Min(a,b) a=min(a,b)
#define fuck(x) cout<<#x<<" - "<<x<<endl
bool vis[11];
int main(){
    //freopen("in.txt","r",stdin);
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scan(T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        int n;scan(n);
        if(n==0){
            puts("INSOMNIA");
            continue;
        }
        int num=0;
        memset(vis,0,sizeof(vis));
        for(int j=1;;j++){
            ll tmp = 1LL*j*n;
            while(tmp){
                if(!vis[tmp%10]) num++;
                vis[tmp%10]=true;
                tmp/=10;
            }
            if(num>=10){
                cout<<(1LL*j*n)<<endl;
                break;
            }
        }
    }
    return 0;
}
