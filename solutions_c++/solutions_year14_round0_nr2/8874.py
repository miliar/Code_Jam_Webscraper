#include <iostream> 
#include <cstdio> 
#include <algorithm> 
#include <cstring> 
#include <string> 
#include <cctype> 
#include <stack> 
#include <queue> 
#include <list> 
#include <vector> 
#include <map> 
#include <sstream> 
#include <cmath> 
#include <bitset> 
#include <utility> 
#include <set> 
#include <numeric> 
#include <iomanip> 
using namespace std; 
double R(double t,double f,double c,double x,double vf){ 
    double t1 = t + (double)x/f; 
    double t2 = t + (double)x/(f+vf) + (double)c/f; 
    if (t1 <= t2 ) return t1; 
    else return R(t+(double)c/f,f+vf,c,x,vf); 
    } 
    
int main () { 
    int t; 
    cin >> t; 
    for (int i =1; i<=t ; i++){ 
        double c,f,x; 
        double t=0; 
        cin >> c >> f >> x; 
        cout << "Case #"<<i<<": ";
        cout << fixed << std::setprecision(7) <<R(0,2,c,x,f)<<endl; 
        } 
    return 0; 
}