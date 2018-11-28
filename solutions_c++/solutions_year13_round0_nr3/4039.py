#include <iostream>
#include <cmath>

using namespace std;

//bool ispali(long int num) {
//    long int n = num;
//    long int rev = 0;
//    long int dig;
//
//    while (num > 0)
//    {
//        dig = num % 10;
//        rev = rev * 10 + dig;
//        num = num / 10;
//    }
//
//    if(rev==n) {
//        return true;
//    } else {
//        return false;
//    }
//
//}

int main() {    

    int t;
    long int a, b;
    long int art, brt;
    long int tot=0;
    long int sq;
    long int array[] = { 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004,
                        404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201,
                        1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};

    cin >> t;

    for(int i=1; i<=t; i++) {
        tot=0;
        cin >> a >> b;

        cout << "Case #" << i << ": ";

        for(int j=0; j<39; j++) {
            if(array[j] >= a && array[j] <= b) {
                tot++;
            }
        }

        cout << tot << endl;
    }

    return 0;
}
