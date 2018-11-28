#include<stdio.h>


int check[15];

int main()
{
    FILE *in,*out;
    int i,j,y,z,t,k,n;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);

    for(i=1;i<=t;i++){

        scanf("%d",&n);

        if(n==0){
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        y=k=0;
        for(j=0;j<10;j++) check[j]=0;


        while(y<10){
            k++;
            z=k*n;
            while(z){
                if(check[z%10]==0){
                    check[z%10]=1;
                    y++;
                }
                z /=10;
            }
        }
        z=n*k;
        printf("Case #%d: %d\n",i,z);


    }


    return 0;
}

