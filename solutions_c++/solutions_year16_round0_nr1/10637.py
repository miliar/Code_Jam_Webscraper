#include <bits/stdc++.h>

using namespace std;

unsigned long long counting_sheep(unsigned long long);

int main() {

    freopen("A-large_output.in", "w", stdout);
    freopen("A-large.in", "r", stdin);

    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        unsigned long long n;
        cin >> n;

        if(n == 0) cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        else cout << "Case #" << i + 1 << ": " << counting_sheep(n) * n << endl;
    }

    fclose(stdout);
    fclose(stdin);

    return 0;
}

unsigned long long counting_sheep(unsigned long long n){

    bool flags[10] = {false};


    unsigned long long counter = 1;
    while(true){
        unsigned long long temp = n * counter;
         //update flags
         while(temp != 0){
            flags[temp % 10] = true;
            temp /= 10;
         }

         //check flags
         bool f = true;
         for(int i = 0; i < 10; i++)
             if(flags[i] == false){
                f = false;
                break;
             }

         if(f) return counter;

         counter++;

    }
}
