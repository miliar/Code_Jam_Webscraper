#include <iostream>
#include <fstream>

using namespace std;

unsigned long answer(unsigned long n){
    if (n == 0) {
        return -1;
    }

    bool seen[11] = {false};
    for (unsigned long i = 1;; i++){
        int temp = n*i;
        while (temp > 0){
            seen[temp%10] = true;
            temp /= 10;
        }

        bool done = true;

        for (int j = 0; j < 10; j++){
            if (seen[j] == false){
                done = false;
                break;
            }
        }

        if (done){
            return i*n;
        }
    }
}

int main(){
    ifstream cin ("input.txt");
    ofstream cout("output.txt");
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n;
        cin >> n;

        cout << "Case #" << (i+1) << ": ";
        int ans = answer(n);
        if (ans == -1) cout << "INSOMNIA"; else cout << ans;
        cout << endl;
    }
    return 0;
}
