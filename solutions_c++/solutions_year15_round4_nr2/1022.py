#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
double eps=0.00000001;
main(){
    ios_base::sync_with_stdio(false);
    int licznik=1;
    int T;
    cin >> T;
    while(T--){
        double res=0;
        int n;
        double V,X;
        cin >> n >> V >> X;
        if(n==1){
            double V1,T1;
            cin >> V1 >> T1;
            if(T1!=X)
                cout << "Case #"<<licznik++<<": IMPOSSIBLE"<< endl;
            else
                cout << "Case #"<<licznik++<<": "<< fixed << setprecision(10) << V/V1 << endl;
        }
        else{
            double V0,T0;
            double V1,T1;
            cin >> V0 >> T0;
            cin >> V1 >> T1;
            if((T1 < X && T0<X) || (T1>X && T0>X)){
                cout << "Case #"<<licznik++<<": IMPOSSIBLE"<< endl;
                continue;
            }
            if(T1==T0){
                res+=V/(V0+V1);
            }
            else{
                double x= V*(X-T0)/(T1-T0);
                if(x<0){
                    cout << "Case #"<<licznik++<<": IMPOSSIBLE"<< endl;
                    continue;
                }
                //cout << x/V1 << ' '<< (V-x)/V0 << endl;
                res=max(x/V1,(V-x)/V0);
            }
            cout << "Case #"<<licznik++<<": "<< fixed << setprecision(10) << res << endl;
        }
    }
    return 0;
}
