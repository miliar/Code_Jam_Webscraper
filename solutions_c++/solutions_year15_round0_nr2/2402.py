#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){


    int t;
    cin>>t;

    int count = 0;

    while(t--){

        count++;
        int n;
        cin>>n;

        int a[n+1];
        int mx = 0;
        for(int i=0;i<n; i++)
        {
            cin>>a[i];
            mx = max(mx,a[i]);
        }

        int mn = mx;
        int minutes = 0;

        for(int i=1 ; i <= mx; i++){
            minutes=i;
            for(int j=0;j<n;j++){
                if(a[j]>i){
                    if( a[j]%i == 0 ){
                        minutes += (a[j]/i -1);
                    }
                    else{
                        minutes += (a[j]/i);
                    }
                }
            }
            mn =min(mn,minutes);
        }
        cout<<"Case #"<<count<<": "<<mn<<endl;
    }
    return 0;
}

