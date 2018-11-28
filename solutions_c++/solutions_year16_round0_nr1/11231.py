#include <iostream>

using namespace std;

int main(){
    long long t, n, w;
    bool digits[10];
    bool check = false;

    cin >> t;

    for(int j = 0; j < t; j++){
        cin >> n;
        for(int x = 0; x < 10; x++)
            digits[x] = false;

        for(int i = 1; i <= 1000000; i++){
            w = n * i;

            long long temp = w;

            do{
                digits[temp % 10] = true;
                temp /= 10;
            }while(temp > 0);

            check = true;

            for(int x = 0; x < 10; x++)
                check = check && digits[x];

            if(check) break;
        }

        if(!check)
            cout << "Case #" << (j+1) << ": INSOMNIA" << endl;
        else
            cout << "Case #" << (j+1) << ": " << w << endl;

    }

    return 0;
}
