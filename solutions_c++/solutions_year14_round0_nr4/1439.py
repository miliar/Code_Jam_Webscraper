#include <iostream>
#include <algorithm>
#include <string.h>
#include <cmath>
#include <stdio.h>

using namespace std;
#define ll long long
#define pb push_back

const int maxn = 2100;
vector<double> a, b;
int n;
vector<int> edge[maxn];
int match[maxn];
bool use[maxn];
bool dfs(int s)
{
    int i;
    for(i=0;i<edge[s].size();i++){
        int x=edge[s][i];
        if(!use[x] ){
            use[x]=true;
            int tmp=match[x];
            match[x]=s;
            if(tmp==-1 || dfs(tmp))
                return true;
            match[x]=tmp;
        }
    }
    return 0;
}
void init(){
    memset(match, -1, sizeof(match));
    for(int i = 0; i < maxn; ++i)
        edge[i].clear();
}
int Match()
{
    int res=0;
    int i;
    for(i=0;  i < n; i++){
        memset(use,0,sizeof(use));
        if(dfs(i))
            res++;
    }
    return res;
}


int main(){
    freopen("Cin.txt", "r", stdin );
    freopen("Cout.txt", "w", stdout );
    int tcase;
    int tno = 0;

    cin>>tcase;
    while( tcase-- ){
        cin>>n;
        a.clear();  b.clear();
        double val;
        for(int i = 0; i < n; ++i){
            cin>>val;
            a.pb( val );
        }
        for(int i = 0; i < n; ++i){
            cin>>val;
            b.pb( val );
        }
        vector<double> x, y;
        x = a;  y = b;
        int war = 0;
        for(int i  = 0;  i < n; ++i){
            int id = -1;
            for(int j = 0; j < y.size(); ++j){
                if( y[j] > x[i] ){
                    if( id == -1 || y[j] < y[id] )
                        id = j;
                }
            }
            if( id == -1 ){
                war++;
                vector<double>::iterator it = min_element(y.begin(), y.end() );
                y.erase(it);

            }else{
                y.erase( y.begin() + id );
            }
        }
        init();
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                if( a[i] > b[j] )
                    edge[i].pb( j );

        int deceit = Match();
        printf("Case #%d: %d %d\n", ++tno, deceit, war );
    }
    return 0;
}
