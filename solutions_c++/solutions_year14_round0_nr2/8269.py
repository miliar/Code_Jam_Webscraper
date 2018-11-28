#include<iostream>
#include<stdio.h>
using namespace std;

int main() {
    int t,testcase=0;
    cin>>t;
    while(t--) {
        testcase++;
        double c,f,x;
        cin>>c>>f>>x;

        double actual_time = x/2.0;
        double rate = 2.0;
        double constVal = 0.0;
        while (true) {
            constVal += c/rate;
            double new_time = 0;
            rate += f;
            new_time = constVal + x/rate;
            if(new_time < actual_time)
                actual_time = new_time;
            else
                break;
        }
        printf("Case #%d: %.7f\n", testcase, actual_time);
        //cout<<"Case #"<<testcase<<": "<<actual_time<<endl;
    }
    return 0;
}
