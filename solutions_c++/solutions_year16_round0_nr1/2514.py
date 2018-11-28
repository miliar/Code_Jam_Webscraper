#include <bits/stdc++.h>
using namespace std;

int N, status;

void mark(long long sum) {
    while(sum > 0) {
        status |= 1<<(sum%10);
        sum /= 10;
    }
}

int main() {
    int TC = 1;
    cin>>TC;
    for(int tc = 1; tc<=TC;tc++) {
        cin>>N;
        if (N!=0) {
            status = 0;
            long long sum = 0;
            while(status != (1<<10) - 1) {
                sum += N;
                mark(sum);
            }
            cout<<"Case #"<<tc<<": "<<sum<<endl;
        } else cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
    }
    return 0;
}
