#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;
double c, f, x;

void process() {
    cin>>c>>f>>x;
    double n = ceil((x-c)/c - 2.0/f);
    int result = n;
    if(result < 0)
        result = 0;
    double ret = x / (double(result*f + 2.0));
    for(int i=result -1;i>=0;i--) {
        ret = ret + c/(double(i*f + 2.0));
    }
    printf("%.7lf\n", ret);
}
int main() {
    int t;
    cin>>t;
    for(int i =0;i<t;i++) {
        cout<<"Case #"<<(i+1)<<": ";
        process();
    }
    return 0;
}