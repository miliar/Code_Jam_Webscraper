#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ITER(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define MOD 1000000007

typedef pair<double,double> ii;
typedef long long int ll;
typedef vector<int> vi;


int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int l=1;l<=T;l++){
        int a,b;
        int A[5][5],B[5][5];
        scanf("%d",&a);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++) scanf("%d",&A[i][j]);
        }
        scanf("%d",&b);
        --a;
        --b;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++) scanf("%d",&B[i][j]);
        }
        int cnt=0,card;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(A[a][i]==B[b][j]) { cnt++; card=A[a][i];}
            }
        }
        if(cnt==1) printf("Case #%d: %d\n",l,card);
        else if(cnt==0) printf("Case #%d: Volunteer cheated!\n",l);
        else printf("Case #%d: Bad magician!\n",l);
    }
return 0;
}
