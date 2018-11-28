#include<cstdio>
#include<cstring>
#include<set>
#include<algorithm>
using namespace std;
int cnt[2505], ans[55], A[110][55];
int main(){
    freopen("input.in","r",stdin);
    freopen("pB_output.txt","w",stdout);
    
    int T, N;
    scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
        printf("Case #%d:",cases);
        scanf("%d",&N);
        set<int> s;
        memset(cnt, 0, sizeof(cnt));
        memset(ans, 0, sizeof(ans));
        for(int i=1; i<=2*N-1; i++){
            for(int j=1; j<=N; j++){
                scanf("%d",&A[i][j]);
                if(!s.count(A[i][j])) s.insert(A[i][j]);
                cnt[A[i][j]]++;
            }
        }
        int a=0;
        set<int>::iterator ite;
        for(ite=s.begin(); ite!=s.end(); ite++){
            if(cnt[*ite]%2==1) ans[a++]=*ite;
        }
        sort(ans, ans+N);
        for(int i=0; i<N; i++) printf(" %d",ans[i]);
        puts("");
    }
    return 0;
}
