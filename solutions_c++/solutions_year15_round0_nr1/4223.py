#include <cstdio>
#include <algorithm>
using namespace std;
int t;
int m;
char a[1003];
int main(){
        scanf("%d",&t);
        FILE* outf = fopen("A.out","w");
        for(int i=1;i<=t;++i){
                int ans = 0;
                int sum = 0;
                scanf("%d%s",&m,a);
                for(int j=1;j<=m;++j){
                        sum=0;
                        for(int k=0;k<j;++k){
                                sum += a[k]-'0';
                        }
                        ans = max(ans,j-sum);
                }
                fprintf(outf, "Case #%d: %d\n",i,ans);
        }
        return 0;
}
