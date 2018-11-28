#include<iostream>
using namespace std;
double cb, C, F, X;
void cheat(int farms, double current_time) {
    double rate = 2 + F*farms;
    double time = X/rate + current_time;
    if(time>cb) {
        return;
    } else {
        cb=time;
        cheat(farms+1, current_time+(C/rate));
    }
}


int main() {
    int T;
    cin>>T;
    for(int i=1;i<=T;++i) {
    cb=999999;
    cin >> C >> F >> X;
    cheat(0,0);
cout.precision(7);
cout.setf(std::ios::fixed, std:: ios::floatfield);
    cout<<"Case #"<<i<<": "<<cb<<endl;
    }
}
