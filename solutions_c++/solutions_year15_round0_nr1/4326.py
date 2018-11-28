#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main() {
    int T = 0;
    cin >> T;

    for(int i=0; i<T; ++i) {
        int smax = 0;
        cin >> smax;
        char num_char = '0';
        int cur_ova = 0;
        int gap = 0;
        for(int j=0; j<=smax; ++j) {
            cin >> num_char;
            int num = num_char - '0';

            if(num == 0) {
                continue;
            }

            if(cur_ova < j) {
                gap += (j - cur_ova);
                cur_ova = j;
            }
            cur_ova += num;
        }

        cout << "Case #" << i+1 << ": " << gap << endl; 
    }

    return 0;
}
