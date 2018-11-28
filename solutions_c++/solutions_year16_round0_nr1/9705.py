#include<iostream>
#include<cstring>
using namespace std;

int main() {
  int T;
  cin >> T;
  int i = 1;
  while ( i <= T) {
    int N;
    int res = 0;
    bool insomnia = false;
    int digits[10];
    fill_n(digits, 10, -1);
    int count = 0;
    cin >> N;
    res = N;
    if (N == 0)
        insomnia = true;
    else {
        int m = 1;
        while(count < 10 ) {
            int n = N * m;
            res = n;
            m++;
            while (count < 10) {
                if (n < 10 ) {
                   if (digits[n] == -1) {
                        digits[n] = n;
                        count++;
                    }

                    break;
                }
                else {
                    int last_digit = n % 10;
                    n = n/10;
                    if (digits[last_digit] == -1 ) {
                        digits[last_digit] = last_digit;
                        count++;
                    }
                }
            }
        }
    }

    cout <<"Case #"<<i<<": ";
    insomnia ? cout<< "INSOMNIA" : cout<< res;
    cout<<endl;
    i++;
  }
}
