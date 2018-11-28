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

int a[102];

int main(){
    int T,A,N;
    freopen("in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int I = 1; I <= T;I++){
        int ans=oo;
        scanf("%d%d",&A,&N);
        for(int i=0;i<N;i++) scanf("%d",&a[i]);
        sort(a,a+N);
        if(A == 1)
        printf("Case #%d: %d\n",I,N);
        else{
            int moves = 0;
            for(int i=0;i<N;i++){
                ans=min(ans,moves+N-i);
                if(a[i]<A) A+=a[i];
                else{
                    while(a[i]>=A){
                        A=(2*A-1) ;
                        ++moves;
                    }
                    A+=a[i];
                }
            }
            ans=min(ans,moves);
            printf("Case #%d: %d\n",I,ans);
        }
    }
    return 0;
}
