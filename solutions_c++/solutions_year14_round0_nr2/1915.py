#include <iostream>
#include <cstdio>
#include<iomanip>

using namespace std;

long double totalCos[1000000];
long double comprCos[1000000];
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int caso;
    cin>>caso;
    for(int i=1;i<=caso;i++){
        long double C, F, X;
        cin>>C>>F>>X;
        comprCos[0]=0;
        totalCos[0]=X/(2+F*0)+comprCos[0];
        comprCos[1]=comprCos[0]+C/(2+F*0);
        totalCos[1]=X/(2+F*1)+comprCos[1];
        int sr=1;
        while(totalCos[sr-1]>totalCos[sr]){
            sr++;
            comprCos[sr]=comprCos[sr-1]+C/(2+F*(sr-1));
            totalCos[sr]=X/(2+F*sr)+comprCos[sr];
        }
        double res=totalCos[sr-1];

        cout<<"Case #"<<i<<fixed<<setprecision(6)<<": "<<res<<endl;
    }
    return 0;
}
