#include<iostream>
#include<cstdio>

using namespace std;

int main(){
        int T,testCase = 1;
        double C,F,X,rate = 2.0,newRate = 2.0,timeElapsed = 0,newTotalTime = 0;
        cin>>T;
        while(testCase <= T){
                //cout<<"\n\n\n"<<testCase<<"\n";
                scanf("%lf %lf %lf",&C,&F,&X);
                //printf("%0.7f %0.7f %0.7f\n",C,F,X);

                rate = 2.0;
                newRate = 0.0;
                timeElapsed = 0.0;
                while(true){
                        newRate = rate + F;
                        //printf("not buy: %0.7f buy: %0.7f ",X/rate, C/rate + X/newRate);
                        if(X/rate < C/rate + X/newRate){
                                timeElapsed += X/rate;
                                break;
                        }
                        else{
                                timeElapsed += C/rate;
                                rate = newRate;
                        }
                        //cout<<" time: "<<timeElapsed<<"\n";
                }
                printf("Case #%d: %0.7lf\n",testCase,timeElapsed);
                testCase++;
        }
}
