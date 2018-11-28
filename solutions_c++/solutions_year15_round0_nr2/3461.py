#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int t,d;
    int a[1000];
    cin >> t;
    for (int i=0;i<t;i++){
        cin >> d;
        int maxa = 0;
        for (int j=0;j<d;j++){
            cin >> a[j];
            if (a[j]>maxa)
                maxa = a[j];
        }
        int ans = maxa;
        for (int j=1;j<=maxa;j++){
            int sum = j;
            for (int k=0;k<d;k++)
                if (a[k]>j){
                    if (a[k]%j==0)
                        sum += a[k]/j-1;
                    else
                        sum +=a[k]/j;
                }
            if (sum < ans)
                ans = sum;
        }
        cout <<"Case #" << i+1 << ": " <<  ans << endl;
    }
    return 0;
}
