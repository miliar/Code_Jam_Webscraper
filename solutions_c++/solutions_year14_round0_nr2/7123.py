#include<stdio.h>
#include<iostream>

using namespace std;

int main(){
    FILE *fp = fopen("B-large.in","r+");
    FILE *fp2 = fopen("output.txt","w+");
    long long int no_of_test_cases;
    //scanf("%lld",&no_of_test_cases);
    int no = 1;
    fscanf(fp,"%lld",&no_of_test_cases);

    while(no_of_test_cases--){
        double C,F,X;
        double multiple = 2.0;
        double time = 0.0;

        //scanf("%lf %lf %lf",&C,&F,&X);
        fscanf(fp,"%lf %lf %lf",&C,&F,&X);

        if(C > X){
            time = X/multiple;
            //printf("Case #%d: %.7lf\n",no++,time);
            fprintf(fp2,"Case #%d: %.7lf\n",no++,time);
            continue;
        }
        double time1=0.0,time2=0.0;
        while(1){
            time1 = time + X/multiple;
            time2 = time + C/multiple + X/(multiple + F);

            if(time1 > time2 ){
                time = time + C/multiple;
                multiple+= F;
            }
            else{
                break;
            }
        }

        //printf("Case #%d: %.7lf\n",no++,time1);
        fprintf(fp2,"Case #%d: %.7lf\n",no++,time1);
    }
    return 0;
}
