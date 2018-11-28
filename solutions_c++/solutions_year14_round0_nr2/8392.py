#include <fstream>
using namespace std;
void cookie() {
    ifstream file("/Users/sborkar/input.in");
    int T;
    double C, F, X;
    file >> T;
    for(int i =0 ; i<T ; i++) {
        file >> C >> F >> X;
        double cur=0.0, rate=2.0, time=0.0;
        while(cur<X) {
            if(cur<C) {
                time+=(C-cur)/rate;
                cur=C;
            }
            if(cur>=C && (X-cur)/rate > (X-(cur-C))/(rate+F)) {
                cur-=C;
                rate+=F;
            }
            else if(cur>=C) {
                time+=(X-cur)/rate;
                cur=X;
            }
        }
        printf("Case #%d: %.7f\n",i+1, time);
    }
}

int main() {
    cookie();
}