#include <iostream>
#include<cstdio>

using namespace std;

int chk[15];

int main()
{
    FILE *in,*out;
    int i,j,x,y,z,t,k,n;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);

    for(i=1;i<=t;i++){
        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        for(j=0;j<10;j++) chk[j]=0;
        y=k=0;
        while(y<10){
            k++;
            z=k*n;
            while(z){
                if(chk[z%10]==0){
                    chk[z%10]=1;
                    y++;
                }
                z /=10;
            }
        }
        printf("Case #%d: %d\n",i,n*k);

    }






    return 0;
}
