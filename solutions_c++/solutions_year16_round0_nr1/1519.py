#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t, num;
    cin>>t;
    for(int test = 1; test <= t; test++){
        cin>>num;
        if(num == 0){
            cout<<"Case #"<<test<<": INSOMNIA"<<endl;
            continue;
        }
        int arr[10] = {0}, c = 2, val = num;
        while(1){
            int f = 0;
            int k = val;
            while(k){
                arr[k%10] = 1;
                k = k/10;
            }
            for(int j = 0; j < 10; j++){
                if(!arr[j]){
                    f = 1;
                    break;
                }
            }
            if(!f){
                cout<<"Case #"<<test<<": "<<val<<endl;
                break;
            }
            val = num*c;
            c++;
        }
    }
}