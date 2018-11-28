#include <iostream>

using namespace std;


int main(){
    int t;
    int n;
    bool found_pos[10];
    int n_found;
    int i;
    int digit;
    cin >> t;
    for(int c = 1; c <= t; c++){
        fill_n(found_pos, 10, false);
        n_found = 0;;
        i = 1;
        cin >> n;
        if(n == 0){
            cout << "Case #" << c << ": INSOMNIA" << endl;
        } else {
            do{
                int tmp = n * i;
                while(tmp >= 10){
                    digit = tmp % 10;
                    tmp = tmp / 10;
                    if(!found_pos[digit]){
                        n_found++;
                    }
                    found_pos[digit] = true;
                }
                digit = tmp;
                if(!found_pos[digit]){
                    n_found++;
                }
                found_pos[digit] = true;
                i++;
            } while(n_found < 10);
            cout << "Case #" << c << ": " << n * (i-1) << endl;
        }
    }
    return 0;
}
