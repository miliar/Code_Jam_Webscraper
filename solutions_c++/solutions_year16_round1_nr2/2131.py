#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int a[55][55];
struct node{
    bool isRow;
    int b[55];
};
node n[110];
int countAlphbet[2550];
int c[55];
int T,N;
int Case = 1;
int main(){
    #ifndef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    scanf("%d",&T);
    while(T--){
        scanf("%d",&N);
        memset(a,0,sizeof(a));
        memset(c,0,sizeof(c));
        memset(countAlphbet,0,sizeof(countAlphbet));
        for(int i=0;i<N*2-1;i++){
            for(int j=0;j<N;j++){
                scanf("%d",&n[i].b[j]);
            }
        }
        for(int i=0;i<N*2-1;i++){
            for(int j=0;j<N;j++){
                countAlphbet[n[i].b[j]]++;
            }
        }
        int index = 0;
        for(int i=1;i<2550;i++){
            if(countAlphbet[i]&1)
                c[index++] = i;
        }
        sort(c,c+N);
        printf("Case #%d:",Case++);
        for(int i=0;i<N;i++)
            printf(" %d",c[i]);
        puts("");
    }
    return 0;
}
