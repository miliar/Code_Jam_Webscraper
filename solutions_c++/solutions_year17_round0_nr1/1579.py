#include <bits/stdc++.h>
using namespace std;
int meh[1050];
int main(){
    int n, k, countah, arns;
    char hue;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &n);
    for(int ja=0; ja<n; ja++){
     //   printf("Running case %d...\n", ja);
        queue<int> hem;
        assert(hem.size()==0);
        countah = 0;
        arns = 0;
        hue = '.';
        while(hue!=' '){
            scanf("%c", &hue);
            if(hue=='+'){
                meh[countah] = 1;
                countah++;
            }else{
            if(hue=='-'){
                meh[countah] = 0;
                countah++;
            }}
        }
        scanf("%d", &k);
        for(int i=0; i<countah; i++){
            if(hem.size()>0){
                if(hem.front()<=i-k){
                    hem.pop();
                }
            }
            if((meh[i]+hem.size())%2==0){
        //        printf("Flipped at %d\n", i);
                hem.push(i);
                arns++;
            }
        }
        while(hem.size()>0){
        //    printf("Hem size larger than 0\n");
         //   printf("Front hem value:%d\n",hem.front());
            if(hem.front()>countah-k){
                printf("Case #%d: IMPOSSIBLE\n", ja+1);
                goto wtf;
            }
            hem.pop();
        }
        printf("Case #%d: %d\n",ja+1, arns);
        wtf:continue;
    }
}
