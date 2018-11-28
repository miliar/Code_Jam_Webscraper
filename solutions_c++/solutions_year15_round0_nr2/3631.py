#include<bits/stdc++.h>
using namespace std;

int main() {
    int i,j,k,run,n;
    cin>>run;

    for(k=1;    k<=run;    k++) {
        int min = INT_MAX;
        int arr[1005];

        cin>>n;

        for(i=1;    i<=n;    i++) {
            cin>>arr[i];
        }

        for(i=1;   i<=1000;    i++) {
            int total = 0;
            for(j=1;    j<=n;   j++) {
                if(arr[j]%i) {
                    total += arr[j]/i;
                }

                else {
                    total += arr[j]/i - 1;
                }
            }

            total += i;

            if (total < min) {
                min = total;
            }
        }

        cout<<"Case #"<<k<<": "<<min<<endl;
    }
    return 0;
}
