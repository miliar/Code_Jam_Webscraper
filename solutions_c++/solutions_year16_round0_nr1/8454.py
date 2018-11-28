// Example program
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int d[10] = {0};

        long long n;
        cin >> n;
        if(n==0) {
            cout <<"Case #"<<i+1<<": " << "INSOMNIA\n";
        } else {
            int digits = 10;
            int c = 0;
            while(digits > 0) {
                c++;
                long long num = n*c;
                while(num>0) {
                    if(d[num%10] == 0) {
                        digits --;
                        d[num%10] = 1;
                    }
                    num = num/10;
                }
            }
            cout <<"Case #"<<i+1<<": "<< n*c << endl;
        }
    }
    return 0;
}
