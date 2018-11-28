#include <stdio.h>
#include <stdlib.h>

int main()
{   freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,N,j;
    int p,q,r;
    j=1;
    int input;
    int origininput;
    int calcu;
    int a[10];
    for(q=0;q<10;q++){
        a[q]=1;
    }
    scanf("%d",&N);
    for(p=0;p<N;p++){
        scanf("%d",&input);
        if (input==0){
                printf("case #%d: INSOMNIA\n",p+1);
                }
        else{
        origininput=input;
        j=input;
        while(1==1){
            calcu=input;
            while(calcu>0){
                  for(i=0;i<10;i++){
                if(calcu%10==i){
                a[i]=0;
            }
                  }
                calcu=calcu/10;
            }

            if(a[0]==0&&a[1]==0&&a[2]==0&&a[3]==0&&a[4]==0&&a[5]==0&&a[6]==0&&a[7]==0&&a[8]==0&&a[9]==0){
                break;
            }
            else {
                    input=input+origininput;
                    j=j+origininput;
        }
    }
        printf("Case #%d: %d\n",p+1,j);
        }
        for(r=0;r<10;r++){
            a[r]=1;
        }
    }
    return 0;
}
