#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("BRevengeOfThePancakes.out","w",stdout);
    int T, cs=0;
    scanf("%d", &T);
    while(T--)
    {
        char str[110];
        scanf("%s", &str);
        int len=strlen(str);
        int s=len;
        int count=0;
        while(s--)
        {
            //int flag=0;
            if(str[s]!='+')
            {
               count++;
               for(int i=len-1;i>=0;i--){
                   if(str[i]=='-')
                    str[i]='+';
                   else
                    str[i]='-';
               }
            }
            /*else{
                for(int j=0;j<len;j++){
                    if(str[j]=='+')
                        flag=1;
                    else{
                        flag=0;
                        break;
                    }
                }
            }

            if(flag==1){
                printf("Case #%d: %d\n", ++cs, count);
                break;
            }*/

        }
        printf("Case #%d: %d\n", ++cs, count);
    }


    return 0;
}
