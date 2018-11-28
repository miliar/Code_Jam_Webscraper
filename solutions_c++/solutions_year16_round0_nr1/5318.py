#include<bits/stdc++.h>
 
using namespace std;

bool array[12];

int main(){
    int t;
    cin >> t;

    int m=1;
    while(t--){
        cout << "Case #" << m << ": ";
        long long int n;
        cin >> n;
        if(n==0){
            cout << "INSOMNIA\n";
        }else{
            memset(array,false,sizeof(array));
            int var=0;
            long long int x=n,y=0;
            while(var<10){
                x = y+n;
                y = x;
            //    cout << x << "\n";
                while(x!=0){
                  if(!array[x%10]){
                    array[x%10]=true;
                    var++;
                  }
                  x/=10;
                }
            }
            cout << y << "\n";
        }
        m++;
    }

    return 0;
}
