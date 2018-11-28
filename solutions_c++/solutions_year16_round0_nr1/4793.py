#include <iostream>
#include <cstdio>
#include <cstring>
#include <stdlib.h>

using namespace std;

int main()
{
    int N=0,T=0;
    bool digit[10];
    bool insom =false;
    int num=0;
    cin >> T;

    for(int i=1;i<=T;i++)
    {
        int cnt=0;
        scanf("%d", &N);
        int re=-1;
        insom=false;
        for(int j=0;j<10;j++)
        {
            digit[j] =false;
        }
        int index=1;
        int ori=N;
        while(cnt<10)
        {
            num=N;
            int k=num%10; ;
            while(num>0){
                if(!digit[k]){
                    digit[k]=true;
                    cnt++;
                    if(cnt==10){
                        re=N;
                        break;
                    }
                }
                num=num/10;
                k=num%10;
            }
            if(N==ori*(index+1))
            {
                insom= true; 
                break;
            }
            index++;
            N=ori*index;
        } 
        printf("Case #%d: ",i);
        if(insom)
            printf("INSOMNIA\n");
        else
            printf("%d\n", re);
    }
    return 0;
}
