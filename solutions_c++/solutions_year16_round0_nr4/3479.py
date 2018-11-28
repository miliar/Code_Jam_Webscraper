#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T=0,K=0,C=0,S=0;
    cin >> T;
    for(int i=1;i<=T;i++)
    {
        bool impossible =false;
        scanf("%d %d %d", &K,&C,&S);
        int re[101];
        int cnt=0;

        if(C==1)
        {
            for(int j=0;j<K;j++)
            {
                re[j] =j+1;
                cnt++;
            }
        }else{
            if(K==1){
                re[0]=1;
                cnt=1;
            }else{
                for(int j=0;j<K-1;j++)
                {
                    cnt++; 
                    re[j]=2+K*j+j;    
                }
            }
        }
        if(cnt>S)
            impossible =true;

        printf("Case #%d: ",i);
        if(impossible)
            printf("IMPOSSIBLE");
        else{
            for(int j=0;j<cnt;j++)
                printf("%d ", re[j]);
        }
        printf("\n");

    }
    return 0;
}
