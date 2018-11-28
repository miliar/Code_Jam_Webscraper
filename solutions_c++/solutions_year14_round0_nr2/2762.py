#include <iostream>
#include <stdio.h>
using namespace std;
double c,f,x;
inline double _work(int n){
    double res = x/(2.0+f*n);
    for(int i=0; i<n; i++){
        res += c/(2.0+f*i);
    }
    return res;
}
int work(int n){
    double tmp1 = _work(n);
    double tmp2 = _work(n-1);
    if(tmp1 >= tmp2) return 0;
    return 1;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++){
        cin>>c>>f>>x;
        int n = 1;
        while(work(n)){
            n *= 2;
        }
        int low = n/2;
        int high = n;
        while(low <= high){
            int mid = (low + high) / 2;
            if(work(mid)) low = mid + 1;
            else high = mid - 1;
        }
        if(high < 0) high = 0;
        cout<<"Case #"<<i<<": ";
        printf("%.7f\n", _work(high));
    }
}
