#include <stdio.h>

using namespace std;

int main()
{
    int i,j,a[17],t1[5][5],t2[5][5],f1,f2,c,r,n,num;
    FILE * out;
    FILE * in;
    out = fopen ("out.txt","w");
    in = fopen ("in.in","r");
    fscanf(in,"%d",&n);
    for(int r=1;r<=n;r++){
        fscanf(in,"%d",&f1);
        c=0;
        for(i=1;i<17;i++)
            a[i]=0;

           for(i=1;i<5;i++)
                for(j=1;j<5;j++){
                    fscanf(in,"%d",&t1[i][j]);
                    if(f1==i){
                        a[t1[i][j]]++;
                    }
                }

            fscanf(in,"%d",&f2);

            for(i=1;i<5;i++)
                for(j=1;j<5;j++){
                    fscanf(in,"%d",&t2[i][j]);
                    if(f2==i){
                        a[t2[i][j]]++;
                    }
                }

            for(i=1;i<17;i++){
                if(a[i]==2){
                    c++;
                    num=i;
                }
            }

            if(c>1){
                fprintf(out,"Case #%d: Bad magician!\n",r);
            }else{
                if(c==1){
                    fprintf(out,"Case #%d: %d\n",r,num);
                }else fprintf(out,"Case #%d: Volunteer cheated!\n",r);
            }

    }
    return 0;
}
