#include <iostream>
#include <iomanip>

using namespace std;

double timefor(int times, double c, double f, double x) {
    double rate = 2.0;
    double tim = 0.0;
    while(times--) {
        tim += c/rate;
        rate += f;
    }
    tim += x/rate;
    return tim;
}

int main(int argc, char const *argv[]) {
    int test_cases,t;
    cin>>test_cases;
    for (t = 1; t <= test_cases; ++t) {
        // Code here
        double t1,t2;
        double c,f,x;

        cin>>c>>f>>x;

        double rate = 2.0;

        t1 = x/rate;

        t2 = timefor(1,c,f,x);

        if(t1>t2) {
            int curtime = 1;
            while(timefor(curtime+1,c,f,x) < timefor(curtime,c,f,x))
                curtime++;

            cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<timefor(curtime,c,f,x)<<endl;    
        } else {
            cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<t1<<endl; 
        }
    }
    return 0;
}