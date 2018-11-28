#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    int tt; /*test case*/
    int f;  /*num of friends*/
    int stand;
    int shyness;
    int smax;
    char s[1005];
    int i;
    freopen("in","r",stdin);
    freopen("outl","w",stdout);
    scanf("%d",&tt);
    for(int j = 1 ; j <= tt ; ++j){
        printf("Case #%d: ",j);
        f = 0, stand = 0, shyness = 0;
        scanf("%d",&smax);
        scanf("%s",&s);
        for( i = 0 ; i <= smax ; ++i){
            stand += s[i]-'0';
            if( stand < i+1 && i != smax){
                f += i+1-stand;
                stand = i+1 ;
            }
        }        
        printf("%d\n",f);
    }
    return 0;
}
