#include <iostream>
#include <cstdlib>
using namespace std;

bool seen(int *digits, int n) {
    for(int i = 0; i < n; i++)
        if(!digits[i])
            return false;
    return true;
}

int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for(int c = 1; c <= t; ++c) {
        int n;
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<c<<": INSOMNIA"<<endl;
            continue;
        }
        int number = 0, digits[10] = {0};
        memset(digits, 0, sizeof(digits));
        while(!seen(digits, 10)){
            number += n;
            int tmp = number;
            while(tmp){
                digits[tmp%10] = 1;
                tmp /= 10;
            }
        }
        cout<<"Case #"<<c<<": "<<number<<endl;
    }
    return 0;
}
