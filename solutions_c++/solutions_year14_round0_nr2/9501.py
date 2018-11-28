#include <stdio.h>

FILE *fin, *fout;
int T;
double rate = 2.0, C, F, X;

void read_solve_write();
double solve(double t, double r);

int main(){
    read_solve_write();
    return 0;
}

void read_solve_write(){
    fin = fopen("B-small-attempt0.in","r");
    fout = fopen("results.txt","w");
        fscanf(fin,"%d\n",&T);
        for(int i = 0; i < T; i++){
            //rate = 2.0;
            //ans = 0;
            fscanf(fin,"%lf %lf %lf\n",&C,&F,&X);
            //printf("%.7lf\n",solve(0,rate));
            fprintf(fout,"Case #%d: %.7lf\n",i+1,solve(0,rate));
        }
    fclose(fout);
    fclose(fin);
}

double solve(double t, double r){
    double wait_time, buy_time, buy_wait_time;
    wait_time = X/r;
    buy_time = C/r;
    buy_wait_time = X/(r+F);
    //printf("SOLVE(%lf,%lf): %lf %lf\n",t,r,wait_time, buy_time + buy_wait_time);
    if(buy_time+buy_wait_time < wait_time){
        return solve(buy_time+t,r+F);
    }else{
        return t+wait_time;
    }
}
