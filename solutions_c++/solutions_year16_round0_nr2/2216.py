#include<stdio.h>
#include<string.h>
///Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/2
FILE *fo = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/2/input.txt","r");
FILE *fp = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/2/output.txt","w");
int main() {
    int n;
    fscanf(fo,"%d",&n);
    int k,i,toggle;
    for(k=1;k<=n;k++){
        char c[110];
        int in[110],len;
        fscanf(fo,"%s",c);
        len = strlen(c);
        for(i=0;i<len;i++){
            if(c[i] == '+') in[i] = 0;
            else in[i] = 1;
        }
        toggle = 0;
        int ans = 0;
        for(i=len-1;i>=0;i--){
            if(in[i] != toggle){
                ans ++;
                toggle = 1 - toggle;
            }
        }
        fprintf(fp,"Case #%d: %d\n",k,ans);
    }
    return 0;
}