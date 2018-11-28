#include <bits/stdc++.h>
using namespace std;

int arr[1001];
int n ;
int v ;

int main(){
    freopen("xx.in", "rt", stdin);
    freopen("A2out.txt", "wt", stdout);
    int t ,x , cas = 0 ;
    cin >> t ;
    while(t--){
        cin >> n ;
        for(int i = 0 ; i < n ; i++){
            cin >> arr[i];
        }
        int s1 = 0 ;
        double ret = 0.0;
        int Max = 0 ;
        for(int i = 1 ; i < n ; i++){
            x = (arr[i-1] - arr[i]);
            x = max(x,0);
            s1+=x;
            if(Max < x)
                Max= x;
        }
        x = Max;
        int s2 = 0 ;
        int t = 0 ;
        for(int i = 0 ; i < n ; i++){
            t = arr[i];
            t = (t- x);
            if(t <= 0 && i != n-1){s2 += arr[i];}
            else if(i != n-1) {s2 += x;}
        }

        printf("Case #%d: %d %d\n",++cas,s1,s2);
    }
}

