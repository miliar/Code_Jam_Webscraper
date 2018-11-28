#include<stdio.h>
FILE *fo = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/3/input.txt","r");
FILE *fp = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Qualificaiton/3/output.txt","w");
int n,j,t,k,pc=0;
unsigned long long int print[550][2];
void print_front(unsigned long long int start){
    int l[33]={0},lc = 0,i;
    while(start != 0){
        l[lc++] = (int)(start%2);
        start /= 2;
    }
    for(i=lc-1;i>=0;i--){
        fprintf(fp,"%d",l[i]);
    }
}
unsigned long long int trans(unsigned long long int start,int num){
    unsigned long long int ans = 0;
    while(start != 0){
        ans = ans * num + (start%2);
        start /= 2;
    }
    return ans;
}
int main(){
    fscanf(fo,"%d",&t);
    fscanf(fo,"%d %d",&n,&j);
    unsigned long long int max = (unsigned long long int)(1ULL << n) - 1;
    unsigned long long int min = (unsigned long long int)(1ULL << (n-1)) + 1;
    unsigned long long int i=3,start,a1,a2;
    bool check,check2;
    int w;
    while(j > pc){
        start = (min / i) * i;
        if(start < min)start += i;
        for(;start <= max;start += i){
            if(start % 2 == 1) {
                check2 = true;
                for (w = 2; w <= 3; w++) {
                    a1 = trans(start, w);
                    a2 = trans(i, w);
                    if (a1 % a2 != 0) {
                        check2 = false;
                        break;
                    }
                }
                if (check2) {
                    check = true;
                    for (k = 0; k < pc; k++) {
                        if (print[k][0] == start) {
                            check = false;
                            break;
                        }
                    }
                    if (check) {
                        print[pc][0] = start;
                        print[pc++][1] = i;
                        if (pc == j)break;
                    }
                }
            }
        }
        i += 2;
    }
    fprintf(fp,"Case #1:\n");
    int q;
    for(q=0;q<pc;q++){
        print_front(print[q][0]);
//        fprintf(fp," %lld",print[q][1]);
        for(w=2;w<=10;w++){
            i = trans(print[q][1],w);
            fprintf(fp," %lld",i);
        }
        fprintf(fp,"\n");
    }
    return 0;
}