#include <stdio.h>
#include <algorithm>

using namespace std;
int ck[2010];

bool f(int a, int b){
    return a>b;
}
int main(void)
{
    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");

    int i,N,n,j,cnt=10000,max1=0,t=0,k;
    fscanf(in,"%d",&N);

    for(i=0;i<N;i++){
        fscanf(in,"%d",&n);
        for(j=0;j<n;j++){
            fscanf(in,"%d",&ck[j]);
            if(max1<ck[j])
                max1=ck[j];
        }
        for(j=1;j<=max1;j++){
            for(k=0;k<n;k++){

                t+=(ck[k]-j)/j;
                if((ck[k]-j)%j>0)
                    t+=1;

            }

            t+=j;

            if(cnt>t)
                cnt=t;
            t=0;

        }



        fprintf(out,"Case #%d: %d\n",i+1,cnt);
        cnt=10000;






    }





}
