#include<iostream>
#include<vector>
#include<iomanip>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
    int t,b=1;
    cin >> t;
    while(t--){
        int i,j=0,l=0,n=1;
        double f1,f2,d=0,k=0,c,f,m,s=0,sum=0;
        cin >> c >> f >> m;
        while(n==1) {
            f1=k+m/(2+d);
            k=k+c/(2+d)+m/(2+f+d);
           // cout << k <<" " << f1 << endl;
            if(f1<=k ){
                sum=sum+m/(2+d);
                cout << fixed << showpoint << setprecision(7);
                cout << "Case #"  << b << ": " << sum << endl;
                break;
            }
            if(f1>k){
                k=k-m/(2+f+d);
                sum=sum+c/(2+d);
            }
                d=d+f;
        }
        b++;
    }
    return 0;
}
