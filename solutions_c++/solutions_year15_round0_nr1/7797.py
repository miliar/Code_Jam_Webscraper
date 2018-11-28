#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i =0;i<t;i++)
    {
        int topLevel;
        int output=0;
        int total=0;
        int temp=0;
        char number[2000];
        scanf("%d",&topLevel);
        scanf("%s",number);
        if(topLevel == 0){
            output = 0;
        }
        else{
            for(int i=1;i<=topLevel;i++){
                int pLevel,cLevel;
                pLevel = (number[i-1]-48);
                total = pLevel + total+temp;
                temp = 0;
                if(number[i]!='0'){
                    cLevel = i;
                }
                else{
                    cLevel = 0;
                }
                if(cLevel>total){
                    temp = cLevel-total;
                    output = temp + output;
                }
            }

        }
       printf("Case #%d: %d\n",i+1,output);
    }

    return 0;
}
