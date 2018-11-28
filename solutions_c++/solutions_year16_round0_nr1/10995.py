#include <cstdio>
#include <cstdlib>
#include <math.h>

using namespace std;

int main () {

    int t;
    scanf("%d",&t);
    int resp = 0;
    for(int i=1;i<=t;i++){

        int vetor[100];
        for(int l=0;l<=10;l++)vetor[l]=0;
        int x;
        scanf("%d",&x);
        if(x==0) {printf("Case #%d: INSOMNIA\n",i);continue;};
       int z=x;

        for(int j=1;j>=1;j++){
            x = z*j;
            resp = 0;
        while(x>1){
                double y;
            int h = x%10;
           // printf("%d-\n",h);
            vetor[h]=1;
         //   if(h==0) printf("-----%d----%d----\n",h,x);
            y = x/10.0;
            x = floor(x/10.0);
           // printf("//%d\n",x);
            if(x<10 && y>=1){
                    int h = x%10;
                    vetor[h]=1;
             //        if(h==0) printf("-----%d----%d----\n",h,x);
               //     printf("%d-\n",h);
                    break;
            }
        }



            for(int k=0;k<=9;k++){
                if(vetor[k]==1)resp++;
            }
            if(resp==10){ printf("Case #%d: %d\n",i,z*j);resp=0;break;}
        }



    }




    return 0;
}
