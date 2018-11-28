#include <iostream>
using namespace std;
int f(int w){
    int mask = 0;
    int now = 0;
    while (mask != 0x3FF) {
        now += w;
        int cpnow = now;
        while (cpnow>0) {
            mask |= (1<< (cpnow % 10));
            cpnow /= 10;
        }
    }
    return now;

}
int main() {
    int nn; 
    cin >> nn;
    for (int i = 1; i<=nn; i++) {
        cout << "Case #"<<i<<": ";
        int t;
        cin >> t;
        if (t==0) cout <<"INSOMNIA"<<endl;
        else cout << f(t)<< endl;
    }
    

    
}
