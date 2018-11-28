#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <string.h>
#include <string>
#include <list>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <utility>

#define pb push_back
#define SZ 57
using namespace std;

typedef long long Long;

struct Node
{
    struct Node* Child[303];
    Node()
    {
        for(int i=0;i<300;i++) Child[i] = NULL;
    }
};

typedef Node* NodePtr;

void Go(string s,int pos,NodePtr cur)
{
    if(pos==s.size())   return ;
    int c = s[pos];
    if(cur->Child[c]==NULL) cur->Child[c] = new Node();
    Go(s , pos+1 , cur->Child[c] );
}

int Back(NodePtr cur) {
    if(cur==NULL) return 0;
    int ret = 1;
    for(int i=0;i<300;i++) ret += Back(cur->Child[i]);
    return ret;
}

int Mask[(1<<10)];
string arr[100];
int n,m;

int dp[(1<<10)][20] , vis[(1<<10)][20] , True;
int way[(1<<10)][20];
const int inf = (1<<20);

const int mod = 1000000007;


int back(int mask,int tot)
{
    if(vis[mask][tot] == True ) return dp[mask][tot];
    vis[mask][tot] = True; dp[mask][tot] = -inf;
    way[mask][tot] = 0;
    if(tot==n) {
        if(mask == (1<<m)-1) {
            dp[mask][tot] = 0;
            way[mask][tot] = 1;
        }
        return dp[mask][tot];
    }

    for(int i=1;i<(1<<m);i++) {
        if( mask & i) continue;
        dp[mask][tot] = max(dp[mask][tot] , Mask[i] + back( (mask | i) , tot+1));

    }
    for(int i=1;i<(1<<m);i++) {
        if( mask & i) continue;
        if(dp[mask][tot] == Mask[i] + back( (mask | i) , tot+1) ) {
            way[mask][tot] += way[(mask | i)][ tot+1];
            way[mask][tot] %= mod;
        }
    }


    return dp[mask][tot];
}


int main()
{
    freopen("D.in","rt",stdin);
    freopen("D.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++) {
        scanf("%d%d",&m,&n);
        for(int i=0;i<m;i++) cin>>arr[i];
        for(int i=0;i<(1<<m);i++) {
            //cout<<i<<endl;
            Mask[i] = 0;
            NodePtr root = new Node();
            for(int j=0;j<m;j++) {
                if((1<<j) & i) Go(arr[j],0,root);
            }
            Mask[i] = Back(root);
            //cout<<i<<" "<<Mask[i]<<endl;
        }
        //continue;

        True++;
        back(0,0);
        printf("Case #%d: %d %d\n",cas,dp[0][0],way[0][0]);

    }


    return 0;
}
