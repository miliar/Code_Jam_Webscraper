#include <iostream>
using namespace std;

void dream(int N) {
    if(N==0) //Only the N==0 case can lead to INSOMNIA
    {
        cout << "INSOMNIA";
        return;
    }

    bool digits [10] = {true,true,true,true,true,true,true,true,true,true};
    int digitsLeft = 10;
    int s=0;
    int tempS,tempDigit;

    while(digitsLeft>0){
        s+=N;
        tempS=s;
        while(tempS>0){
            tempDigit=tempS%10;
            if(digits[tempDigit])
            {
                digits[tempDigit]=false;
                digitsLeft--;
            }

            tempS/=10;

        }
    }

    cout << s;
}

int main() {
  int t, N, m;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> N;
    cout << "Case #" << i << ": ";
    dream(N);
    cout << endl;
  }
}
