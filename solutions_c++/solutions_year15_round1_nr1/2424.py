#include <bits/stdc++.h>
#define MAX 1001

using namespace std;

int a[MAX];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A_large.out","w",stdout);
    int t,n;
    cin >> t;
    for(int x=1; x<=t; x++){
        cin >> n;
        for(int i=0; i<n; i++) cin >> a[i];
        int minm1 = 0, minm2 = 0;
        int acm = 0;
        int lol = 0;
        for(int i=0; i<n-1; i++){
            if( a[i] > a[i+1] ){
                minm1 += a[i]-a[i+1];
                lol = max(lol,a[i]-a[i+1]);
            }
        }



        for(int i=0; i<n-1; i++){

            minm2 += min(a[i],lol);
        }




        cout << "Case #"<<x<<": "<< minm1 << " " << minm2 << endl;
    }
}
