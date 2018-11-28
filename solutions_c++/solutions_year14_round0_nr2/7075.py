#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("inp1.in","r",stdin);
    int t;
    cin>>t;
    cout.precision(7);
    cout << fixed;

    int a = 1;
    while(a <= t) {
        double c , f , x;
        cin>>c>>f>>x;
        double  rate = 2.0;
        double time = 0.0;
        double v1=0.0 , v2=0.0;
        v1 = x / rate;
        v2 = (c/rate) + (x / (rate+f));
        while(v1 > v2) {
            time += c/rate;
            rate = rate + f;
            v1 = x / rate;
            v2 = (c/rate) + (x / (rate+f));
        }
        time += v1;
        cout<<"Case #"<<a<<": "<<time<<endl;
        a++;
    }
}
