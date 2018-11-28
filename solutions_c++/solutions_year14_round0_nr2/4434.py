#include<iostream>
#include <iomanip>
#include <cstdio>
using namespace std;
int main(){
    if (fopen("input.txt", "r")) freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int N;
    cin>>N;
    for (int i =1; i<=N; i++){
        double C,F,X;
        cout<<"Case #"<<i<<": ";
        cin>>C>>F>>X;
        if (C>=X){
            cout << fixed << setprecision(7) << double(X/2.0) << endl;
        }
        else{
            double ans = 0.0;
            double rate = 2.0;
            while (true){
                double t1 = (X)/rate;
                double t2 = (C)/rate;
                t2+= (X)/(rate+F);
                if (t2>t1){
                    ans+=t1;
                    break;
                }
                else{
                    ans+=(C)/rate;
                    rate+=F;
                }
            }
            cout<< fixed << setprecision(7)<<ans<<endl;
        }
    }
}
