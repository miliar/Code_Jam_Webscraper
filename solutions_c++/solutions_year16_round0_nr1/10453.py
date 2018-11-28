#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int seenDigit[10];
    int t;
    cin>>t;
    for(int i=0; i<t; i++){
        for(int j=0; j<10; j++) seenDigit[j] = 0;
        int n;
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int mul = 1;
        bool found = false;
        int result;
        int digitCounter = 0;
        while(!found){
            int num = n*mul;
            while(num){
                int digit = num % 10;
                if(seenDigit[digit] == 0){
                    seenDigit[digit] = 1;
                    digitCounter++;
                }
                num /= 10;
            }
            mul++;
            if(digitCounter >= 10){
                found = true;
                result = n*(mul-1);
            }
        }
        if(found){
            cout<<"Case #"<<i+1<<": "<<result<<endl;
        }

    }
}
