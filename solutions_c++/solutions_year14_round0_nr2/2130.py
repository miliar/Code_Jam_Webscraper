#include<iostream>
#include<vector>
#include<cmath>
#include<iomanip>

using namespace std; 

int eps(double x, double y){
    double d = x-y; 
    double epson = 10e-6; 
    if(d > -1*epson && d < epson)
        return 0; 
    double dd = d/x; 
    double ddd = d/y;   
    if(dd > -1*epson && dd < epson)
        return 0; 
    if(ddd > -1 * epson && ddd < epson)
        return 0;
    //if(x < y) 
    if(x < y )
        return -1; 
    else 
        return 1; 
}

double work(double c, double f , double x){
    double re = 0; 
    double p = 2.0; 
    while(true){
        double t1 = x/p; 
        double t2 = c/p + x/(p+f); 
        //if(eps(t1,t2) < 0){
        if(t1 < t2){
            re  += t1; 
            break;
        }else {
            re += c/p; 
            p += f; 
        }

    }
    return re; 
}

int main(){
    int T; 
    cin >> T; 
    for(int t = 1; t <= T; t++){
        double c,f,x; 
        cin >> c >> f >> x; 
        cout << "Case #" << t << ": " << fixed << setprecision(7) << work(c,f,x) << endl; 
    }
}
