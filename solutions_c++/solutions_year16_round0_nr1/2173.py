#include <stdio.h>
///Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/1
FILE *fo = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/1/input.txt","r");
FILE *fp = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/1/output.txt","w");

int main() {
    int check = 0,in = 0,max = (1 << 10) - 1,n,cp,gap;
    fscanf(fo,"%d",&n);
    int i,j;
    for(i=1;i<=n;i++){
        fscanf(fo,"%d",&in);
        check = 0;
        if(in != 0){
            int start = 0;
            while(check != max){
                start += in;
                cp = start;
                while(cp != 0){
                    gap = cp % 10;
                    check = check | (1 << gap);
                    cp /= 10;
                }
            }
            fprintf(fp,"Case #%d: %d\n",i,start);
        }else{
            fprintf(fp,"Case #%d: INSOMNIA\n",i);
        }
    }
    return 0;
}