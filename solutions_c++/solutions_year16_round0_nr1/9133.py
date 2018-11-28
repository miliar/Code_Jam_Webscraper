#include <iostream>
#include<fstream>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    int N;
    cin>> t;
    for(int testCase = 1 ; testCase <= t; ++testCase)
    {
        cin >> N;
        if(N == 0) {
            cout<<"Case #"<<testCase<<": INSOMNIA"<<endl;
            continue;
        }
        bool digits[10] = {false};
        for(int i = 1;; ++i) {
            int x = i * N;
            int tmp = x;
            while(x > 0) {
                int d = x % 10;
                x /= 10;
                digits[d] = true;
            }
            bool isSleep = false;
            for(int k = 0; k < 10; ++k) {
                if(digits[k] == false) {
                    break;
                } else if(k == 9) {
                    isSleep = true;
                }
            }
            if(isSleep){
                cout<<"Case #"<<testCase<<": "<<tmp<<endl;
                break;
            }
        }
    }
    return 0;
}
