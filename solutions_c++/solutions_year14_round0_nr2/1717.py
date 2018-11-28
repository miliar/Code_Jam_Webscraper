#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    long long int t;
    cin >> t;
    for(long long int q=1;q<=t;++q){
        double total = 0;
        double c,f,x,rate = 2;
        cin >> c >> f >> x;
        double c_time,x_time,next_time;
        while(1){
            c_time = c/rate;
            x_time = x/rate;
            double temp = rate+f;
            next_time = x/temp;
            if(next_time+c_time < x_time)
            {
                rate+=f;
                total+=c_time;
            }
            else{
                total += x_time;
                break;
            }
        }
        cout.precision(7);
        cout.setf(ios::fixed, ios::floatfield );
        cout << "Case #" << q << ": "  << total << endl;
    }
    return 0;
}
