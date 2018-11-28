#include    <iostream>
#include    <cstdio>
#include    <cstdlib>
#include    <cstring>
#include    <cmath>
#include    <algorithm>
#include    <vector>
#include    <list>
#include    <queue>
#include    <stack>
#include    <map>
#include    <set>
#include    <utility>
#include    <climits>
#include    <cfloat>
#include    <cassert>
#define     read(n)         scanf("%d",&n)
#define     read2(n,m)      scanf("%d%d",&n,&m)
#define     read3(n,m,l)    scanf("%d%d%d",&n,&m,&l)
#define     readull(n)      scanf("%llu",&n)
#define     readll(n)       scanf("%lld",&n)
#define     init(mem)       memset(mem,0,sizeof(mem))
#define     ull             unsigned long long int
#define     ll              long long int
#define     vi              vector<int>
#define     vs              vector<string>
using namespace std;
//std::cout.sync_with_stdio(false);

int main(){
    int grass[100][100];
    int t,n,m;
    read(t);
    for(int ii=1;ii<=t;ii++){
        read2(n,m);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                read(grass[i][j]);
            }
        }
        bool gok=true;

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                bool ok=true;
                for(int k=0;k<m;k++){
                    if(grass[i][k]>grass[i][j]) ok=false;
                }
                if(ok) continue;
                ok=true;
                for(int k=0;k<n;k++){
                    if(grass[k][j]>grass[i][j]) ok=false;
                }
                if(!ok) gok=false;
            }
        }
        if(gok){
            printf("Case #%d: YES\n",ii);
        }
        else{
            printf("Case #%d: NO\n",ii);
        }
    }
    return 0;
}
