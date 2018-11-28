#include<iostream>
using namespace std;
int find(int n) {
    int all = 0;
    int cur = n;
    while(true) {
        int tmp = cur;
        do {
            all |= (1<<(tmp%10));
            tmp/=10;
        } while(tmp);
        if(all == 1023) break;
        cur+=n;
    }
    return cur;
}
int main() {
    int n = 0;
    int num;
    cin >> n;
    for(int i =0 ;i < n ;++i) {
        cin >> num;
        if(num == 0) 
            cout << "Case #" << (i+1) << ": INSOMNIA"<< endl;
        else cout << "Case #" << (i+1) << ": " << find(num) << endl;
    }
}
