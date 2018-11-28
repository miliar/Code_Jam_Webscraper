#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    char in[101];

    scanf("%d",&T);

    for(int i=1;i<=T;i++){
        scanf("%s",&in);

        char tanda;
        int lastI, ln=strlen(in), j=0, loop=0;

        while(1){
            j=0;
            if(in[j]=='+'){
                tanda='+';
            }else{
                tanda='-';
            }

            while(j<ln && in[j]==tanda )j++;

            if(tanda=='-'){
                for(int k=0;k<j;k++)in[k]='+';
                loop++;
            }else if(tanda=='+'){
                if(j!=ln){
                    for(int k=0;k<j;k++)in[k]='-';
                    loop++;
                }else{
                    break;
                }
            }
        }



        printf("Case #%d: %d\n",i,loop);
    }
    return 0;
}
