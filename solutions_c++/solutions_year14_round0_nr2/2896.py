#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int round=0,r=1;
    double rate=2,cost=0,incrate=0,goal=0,curtime=0,lasttime=0,costtime=0;
    FILE *fp, *wfp;
    fp=fopen("B-large.in","r+");
    wfp=fopen("B-large.out","w+");
    fscanf(fp,"%d",&round);
    while(r<=round){
        fscanf(fp,"%lf %lf %lf",&cost,&incrate,&goal);
        curtime=0,lasttime=0,rate=2,costtime=cost/rate;
        lasttime=goal/rate;
        while(1){
            rate+=incrate;
            curtime=goal/rate+costtime;
            costtime+=cost/rate;
            if(curtime>=lasttime)
                break;
            else lasttime=curtime;
        }
        fprintf(wfp,"Case #%d: %.7lf\n",r,lasttime);
        r++;
    }
    fclose(fp);
    fclose(wfp);
    return 0;
}
