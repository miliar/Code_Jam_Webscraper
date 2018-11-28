#include<iostream>
#include<math.h>
using namespace std;
int arr [1005];

int main () {

    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    int n,y,z,diff;
    double rate;
    int max_rate;
    for (int i=1;i<=t;i++) {

        cin>>n;
        for (int j=0;j<n;j++) {
            cin>>arr[j];
        }
        max_rate = 0;
        for (int j=1;j<n;j++) {
            if (arr[j-1]>arr[j]) {
                diff = arr[j-1]- arr[j];
                rate = (double)diff/10.0;
                max_rate = max (diff,max_rate);
            }

        }
        //cout<<"rate="<<max_rate<<endl;
        long long eaten=0;
        //int eat= 10 * max_rate;
        int eat = max_rate;
        for (int j=0;j<n-1;j++) {
            eaten += min ( eat,arr[j]);

        }
        z=eaten;
        eaten =0;
        for (int j =1;j<n;j++) {
            if (arr[j-1]>arr[j]) {
                eaten += arr [j-1] - arr[j];
            }
        }
        y = eaten;

        cout<<"Case #"<<i<<":  "<<y<<"  "<<z<<endl;
    }
}
