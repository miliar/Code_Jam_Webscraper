#include <stdio.h>
#include <string.h>
#include <stack>

using namespace std;


int main(){

    int a;
    //freopen("input.in","r",stdin);
    //freopen("input.out","w",stdout);
    scanf("%d",&a);
    for(int j = 0; j < a;j++){
        char str[100],t;
        scanf("%c",&t);
        scanf("%[^\n]",str);

        int ans = 0;
        bool ind = false;
        int ind2 = 0;
        for( ind2 = 0; ind2 < strlen(str) && (str[ind2] == '+');ind2++);
        if(ind2 == strlen(str)) ans = 0;
        else {
            do{

                ans++;
                char first = str[0];
                if( first == '-'){
                    str[0] = '+';
                    for( ind2 = 1; ind2 < strlen(str) ;ind2++){
                        if( str[ind2] == '-') str[ind2] = '+';
                        else break;

                    }
                    for( ind2 = 0; ind2 < strlen(str) && (str[ind2] == '+');ind2++);
                }
                else {
                    str[0]  = '-';
                    for( ind2 = 1; ind2 < strlen(str) ;ind2++){
                        if( str[ind2] == '+') str[ind2] = '-';
                        else break;
                    }
                    for( ind2 = 0; ind2 < strlen(str) && (str[ind2] == '+');ind2++);
                }

                if(ind2 == strlen(str)) break;

            }while(1);
        }
        printf("Case #%d: %d\n",j+1,ans);

    }
}
