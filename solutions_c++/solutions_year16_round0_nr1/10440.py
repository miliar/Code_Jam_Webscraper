#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        long long int n;
        cin >> n;
        if(!n){
            cout<<"Case #"<<a0+1<<": "<<"INSOMNIA"<<endl;
        }
        else{
            int digits[10]={0},count=0;
            long long int i=0;
            while(count!=10){
                i++;
                long long int x = n*i;
                while(x){
                    int d = x%10;
                    x/=10;
                    if(!digits[d])
                        count++;
                    digits[d]=1;
                }
            }
            cout<<"Case #"<<a0+1<<": "<<n*i<<endl;
        }
    }
    return 0;
}
