#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("inputA.in", "r", stdin);
    freopen("outputA.out", "w", stdout);
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++){
        int n;
        long long cur = 0;
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
            continue;
        }
        int mask = (1 << 10) - 1;
        while(mask){
            cur += n;
            long long temp = cur;
            while(temp){
                mask &= ~(1 << (temp % 10));
                temp /= 10;
            }
        }
        cout<<"Case #"<<t<<": "<<cur<<endl;
    }
    return 0;
}
