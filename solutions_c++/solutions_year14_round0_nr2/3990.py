#include <iostream>
#include <vector>
using namespace std;

int main() {
    cout.setf(ios::fixed);
    cout.precision(7);
    int t;
    cin >> t;
    for (int cas = 1; cas<=t; cas++) {
        cout << "Case #" << cas << ": ";
        double c,f,x;
        cin >> c >> f >> x;
        vector<double> v(int(x/c)+2);
        v[0] = x/2;
        for (int i=1; i<v.size(); i++) {
            v[i] = v[i-1] - x/(2+(i-1)*f) + x/(2+i*f) + c/(2+(i-1)*f);
        }
        double min = 999999999;
        for (int i=0; i<v.size(); i++) {
            if (v[i] < min) min = v[i];    
        }
        cout << min << endl;
    }   
}
