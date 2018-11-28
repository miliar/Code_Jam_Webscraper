#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<string>
#include<iterator>
#include<string>
#include<sstream>
#include<cassert>
#include<ctime>
#include<cmath>

#define MP make_pair
#define PB push_back
#define X first
#define Y second
#define oo 2000000000
#define MOD 1000000007
#define LL long long int
#define PII pair<int,int>
#define DEBUG 0

using namespace std;

int ar[102][102];

int main(){
    int T,N,M;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        scanf("%d%d",&N,&M);
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++) scanf("%d",&ar[i][j]);
        }
        bool valid = true;
        for(int i=0;i<N && valid;i++){
            for(int j=0;j<M && valid;j++){
                bool yes = true;
                for(int k=0;k<N;k++) yes &= (ar[k][j] <= ar[i][j]);
                if(!yes){
                    yes = true;
                    for(int k=0;k<M;k++) yes &= (ar[i][k] <= ar[i][j]);
                    if(!yes) valid = false;
                }
            }
        }
        printf("Case #%d: ",I);
        puts(valid ? "YES" : "NO");
    }
    return 0;
}
