#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int T, i, j, count;
    T = 0;
    long long int a, b;
    long long int fs[] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
    cin >> T;
    for (i=0;i<T;i++){
        count = 0;
        cin >> a >> b;
        for (j=0;fs[j];j++){
            if (fs[j] > sqrt(b)) break;
            if (fs[j]>=sqrt(a) && fs[j]<=sqrt(b)) count++;
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
}
