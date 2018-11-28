#include <iostream>
using namespace std;
bool digits[10];
void set(int);
int check();
int last();
int main() {
    cin.tie(0); ios_base::sync_with_stdio(0);
    int test,number,n,cnum,no,l;
    cin >> test;
    for(int t=1;t<=test;t++) {
        cin >> number;
        if(number == 0) cout << "Case #" << t << ": INSOMNIA\n";
        else {
            n = 1;
            no = 10;
            digits[0] = digits[1] = digits[2] = digits[3] = digits[4] = digits[5] = digits[6] = digits[7] = digits[8] = digits[9] = false;
            while (no > 1) {
                set(number*n++);
                no = check();
            }
            l = last();
            while (!digits[l]) {
                set(number*n++);
            }
            cout << "Case #" << t << ": " << number*(n-1) << "\n";
        }
    }
}
void set(int number) {
    while(number > 0) {
        digits[number%10] = true;
        number /= 10;
    }
}
int check() {
    int t = 0;
    for(int i=0;i<10;i++) {
        if(!digits[i]) t++;
    }
    return t;
}
int last() {
    for(int i=0;i<10;i++) {
        if(!digits[i]) return i;
    }
}
