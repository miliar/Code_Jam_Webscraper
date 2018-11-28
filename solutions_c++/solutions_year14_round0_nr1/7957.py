#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;
int main(){
    int T,r,cas=0,tmp,res,ans;
    int cards[5];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        cas++;
        scanf("%d", &r);
        for(int i=1;i<=4;i++){
            
            for(int J=0;J<4;J++)
                if(i==r)
                        scanf("%d",&cards[J]);
                else
                    scanf("%d",&tmp);
        }
        res = 0;
        scanf("%d",&r);
        
        for(int i=1;i<=4;i++){
            
            for(int J=0;J<4;J++){
               scanf("%d",&tmp);
               if(r==i){
                   for(int k =0;k<4;k++)
                       if(tmp==cards[k]){
                           res++;
                           ans = tmp;
                       }
                   
               }
            }
        }
        printf("Case #%d: ", cas);
        switch(res){
            case 0: printf("Volunteer cheated!\n");break;
            case 1: printf("%d\n",ans);break;
            default: printf("Bad magician!\n");
            
        }
    }
    
}
