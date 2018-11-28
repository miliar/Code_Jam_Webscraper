#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct Water {
    double rate, temp;
    Water():rate(-1),temp(-1) {}
};

double max(double x, double y)
{
    return x<y?y:x;
}

int main()
{
    int T, Tcnt=1;
    cin>>T;
    for(; T; T--,Tcnt++) {
        int N;
        double V, X;
        cin>>N>>V>>X;
        vector<Water> waters;
        for(int i=0; i<N; i++) {
            Water n;
            cin>>n.rate>>n.temp;
            waters.push_back(n);
        }
        if(N==2 && fabs(waters[0].temp - waters[1].temp)<1e-8) {
            N--;
            waters[0].rate += waters[1].rate;
        }
        if(N==1) {
            if(X != waters[0].temp) {
                cout << "Case #"<<Tcnt<<": IMPOSSIBLE"<<endl;
            } else {
                printf("Case #%d: %.9lf\n", Tcnt, V/waters[0].rate);
            }
        } else {
            double v0 = V*(waters[1].temp-X)/(waters[1].temp-waters[0].temp);
            double v1 = V*(X-waters[0].temp)/(waters[1].temp-waters[0].temp);
            if(v0<-1e-8 || v1<-1e-8) {
                cout << "Case #"<<Tcnt<<": IMPOSSIBLE"<<endl;
            } else {
                printf("Case #%d: %.9lf\n", Tcnt, max(v0/waters[0].rate, v1/waters[1].rate));
            }
        }
    }
    return 0;
}

