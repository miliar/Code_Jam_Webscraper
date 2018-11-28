#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int Map[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,nn,numCnt;
    scanf("%d",&t);

    for(int i = 1; i <= t; i++){
        //n = i;
        scanf("%d",&n);
        numCnt = 0;
        nn = n;
        if(!n){
            printf("Case #%d: INSOMNIA\n",i);
        }
        else
        while(1){
            int k=nn,c;
            while(k!=0){
                c = k%10;
                if(Map[c] != i){
                    Map[c] = i;
                    numCnt++;
                }
                k /= 10;
            }
            if(numCnt == 10){
                //if(nn < 0)
                printf("Case #%d: %d\n",i,nn);
                break;
            }
            nn += n;
        }
    }

    return 0;
}
