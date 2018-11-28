
#include<stdio.h>
#include <algorithm>
#include <string.h>


using namespace std;
char str[101];
int n,l;

int main(){
    int T,ans,cons;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=0; t<T; t++){

        scanf("%s%d",&str,&n);
        l = strlen(str);
        //l--;
        ans = 0;
        //printf("length is %d and %d",l,n);
        //printf("original string is %s\n",str);
        for(int i=0; i<l; i++){
            for(int j=i; j<l; j++){
                cons = 0;

                    for(int x=i; x<=j; x++){
                    if( (str[x] == 'a')||(str[x]=='i')|| (str[x]=='e')||(str[x]=='o')||(str[x]=='u') ){
                        cons = 0;
                    }
                    else cons++;
                    if(cons >= n){
                        ans++;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",t+1, ans);
    }

return 0;
}
