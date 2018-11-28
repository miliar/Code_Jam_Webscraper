#include <iostream>

using namespace std;

int main() {
    int T=0;
    cin>>T;
    for(int j=1; j<=T; j++) {
        double C,F,X;
        cin>>C>>F>>X;
        C *= 1000000;
        X *= 1000000;
        double speed=2, atime=0, btime=X/speed, prev=atime+btime, curr=prev;
        while(curr<=prev) {
            atime += C/speed;
            speed += F;
            btime = X/speed;
            prev = curr;
            curr = atime+btime;
        }
        printf("Case #%d: %.7f\n",j,prev/1000000);
    }
}
