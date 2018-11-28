#include<iostream>

using namespace std;

int main(){
    double EPS =  1e-7;
    int t;
    double c, f, x, tmp;
    cin >> t;
    for(int i=1; i<=t; i++){
        cin >> c >> f >> x;
        double rate = 2.0;
        double time = 0;
        while(true){
            double time1 =  x/rate;
            double time2 =  c/rate + x/(rate+f);
            if(time2 > time1 + EPS){
                time += time1;
                break;
            }
            else{
                time += c/rate;
                rate += f;
            }
        }
        cout << "Case #"<<i<<": ";
        cout << fixed;
        cout.precision(7);
        cout << time << endl;
        cout.unsetf(ios_base::floatfield);
    }
    return 0;

}
