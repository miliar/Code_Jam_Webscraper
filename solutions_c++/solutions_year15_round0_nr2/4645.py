#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
int arr[5000] ;
int main() {
    int t,cas=0 ;
    int n,maxi,mini,sum ;


    cin >> t ;
    while(t--) {
        cin >> n ;
        for(int i=0;i<n;i++){
            cin>>arr[i] ;
            maxi=max(maxi,arr[i]) ;
        }
        mini=maxi ;
        for(int i=1;i<=maxi;i++) {
            sum=i;
            for(int j=0;j<n;j++) {
                if(arr[j]>i) {
                    if(arr[j]%i== 0){
                        sum+=arr[j]/i-1;
                    }
                    else{
                        sum+=arr[j]/i;
                    }
                }
            }
            mini = min(mini,sum) ;
        }
        cout << "Case #"<<++cas<<": "<<mini<<endl ;
    }
    return 0 ;
}
