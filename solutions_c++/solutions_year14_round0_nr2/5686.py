#include<iostream>
#include<iomanip>
using namespace std;

int main() {
    int T;
    double C,X,F,R;
    double threshold, count;
    
    cin>>T;
    for (int num = 1; num <= T; ++ num) {
        count = 0; R=2;
        cin>>C>>F>>X;
        threshold = (X-C)*F/C;
        
        while (R<threshold) {
            count += C/R;
            R += F;
        }
        count += X/R;
        
        cout<<"Case #"<<num<<": "<<fixed<<setprecision(7)<<count<<endl;
    }
}
