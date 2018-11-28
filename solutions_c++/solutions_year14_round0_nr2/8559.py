#include <stdio.h>
int main(void) {
    FILE* in=fopen("B-large.in","r");
    FILE* out=fopen("output.txt","w");
    int tests,farms;
    double cost,byFarm,need,totalTime,time1,time2,time3;
    fscanf(in,"%d",&tests);
    for(int i=0;i<tests;++i) {
        printf("%d\n",i);
        fscanf(in,"%lf %lf %lf",&cost,&byFarm,&need);
        farms=0;
        totalTime=0.;
        time1=need/2.;
        time2=cost/2.;
        time3=need/(2.+byFarm);
        while(time1>(time2+time3)) {
            totalTime+=time2;
            ++farms;
            time1=need/(farms*byFarm+2.);
            time2=cost/(farms*byFarm+2.);
            time3=need/((farms+1)*byFarm+2.);
        }
        totalTime+=time1;
        fprintf(out,"Case #%d: %.7lf\n",i+1,totalTime);
    }
    fclose(in);
    fclose(out);
    return 0;
}
