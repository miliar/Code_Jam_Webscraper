#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	cout<<setprecision(10);
	
    int t, i,k;
    double c, f, x, rate, time;
    cin>>t;
    k = 1;
    for (i = 0; i < t; i++) {
      
       
        cin>>c>>f>>x;
        rate = 2.0;
        time = 0.0;
        while ((x/rate) > (c/rate) + (x/(rate+f))) {
            time = time + (c/rate);
            rate = rate + f;
        }
        time =  time + (x/rate);
       cout<<"Case #"<<k<<": "<<time<<"\n";
        k++;
    }
    return 0;
}
