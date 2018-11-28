#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;

double d[205];

double p[205][205];

double poss(vector<double>&x){
    memset(p,0,sizeof(p));
    p[0][0]=1;
    for(int i=1;i<=(int)x.size();i++){
        double gl=x[i-1];
        p[i][0]=p[i-1][0]*(1-gl);
        for(int j=1;j<=i;j++){
            p[i][j]=p[i-1][j]*(1-gl)+p[i-1][j-1]*gl;
        }
    }
    return p[x.size()][x.size()/2];
}

int n,k;
vector<double> ans;
double best;
void dfs(int i){
    if(ans.size()==k){
        best=max(best,poss(ans));
        return;
    }
    if(ans.size()+n-i<k)return;
    if(i==n)return;
    dfs(i+1);
    ans.push_back(d[i]);
    dfs(i+1);
    ans.pop_back();
}

void greedy(){
    for(int x=0;x<=k;x++){
        vector<double> t;
        for(int i=0;i<x;i++){
            t.push_back(d[i]);
        }
        for(int i=0;i<k-x;i++){
            t.push_back(d[n-1-i]);
        }
        best=max(best,poss(t));
    }
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int T,Case=1;
    for(scanf("%d",&T);Case<=T;Case++){
        scanf("%d%d",&n,&k);
        best=0.0;
        for(int i=0;i<n;i++){
            scanf("%lf",&d[i]);
        }
        sort(d,d+n);
        //dfs(0);
        greedy();
        printf("Case #%d: %.8f\n",Case,best);
    }
    return 0;
}

