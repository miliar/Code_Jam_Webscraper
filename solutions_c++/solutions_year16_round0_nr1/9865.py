#include <iostream>
#include <map>
using namespace std;

bool check(int a[]) {
    for (int i=0; i<10; i++) {
        if (a[i]==0) {
            return true;
        }
    }
    return false;
}

int result(long long int n) {
    int a[10];
    for(int i=0; i<10; i++) {
        a[i] = 0;
    }
    long long int n_orig = n;
    while(check(a)) {
        long long int temp = n;
        while(temp) {
            a[temp%10]++;
            temp /= 10;
        }
        n += n_orig;
    }
    return (n-n_orig);
}


int main() {
    int t;
    cin>>t;
    int i=0;
    while(t--) {
        i++;
        long long int n;
        cin>>n;
        if(n==0) {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else {
            cout<<"Case #"<<i<<": "<<result(n)<<endl;
        }
    }
    return 0;
}
