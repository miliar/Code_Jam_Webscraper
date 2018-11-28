#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
    freopen("input.txt" , "r" , stdin) ;
    freopen("output.txt" , "w" , stdout) ;

    int t , CASE = 0 ;
    ll n , x , y , z , tmp ;
    cin >> t ;
    while(t--){
        cin >> n ;
        int arr[12];
        memset(arr,0,sizeof(arr));
        cout <<"Case #"<<++CASE<<": " ;
        if(n == 0){
            cout << "INSOMNIA"<<endl;
        }
        else{
            x = n ;
            z = 0 ;
            tmp = x ;
            while(z != 10){
                y = x ;
                tmp = x ;
                while(y){
                    if(arr[y%10] == false){
                        arr[y%10] = true ;
                        z++ ;
                    }
                    y /= 10 ;
                }
                x += n ;
            }
            cout << tmp << endl ;
        }
    }
}
