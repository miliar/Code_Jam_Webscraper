#include <iostream>

using namespace std;

void countSheep(int n){
    int seen[10] = {0}; //Array of 0s to keep track of which have been seen
    int pass = 10; //this will be number of digits to be seen
    int curr = n;
    int digit = 0, i = 0;
    int temp = n;
    while(true){
        ++i;
        curr = i * temp;
        n = curr;

        while(n != 0){
            digit = n%10;
            if(seen[digit] == 0){
                --pass;
            }
            seen[digit] = 1;
            n /= 10;
        }
        if(i > 10000){
            cout << "INSOMNIA" << endl;
            return;
        }else if(pass == 0){
            cout << curr << endl;
            return;
        }
    }
}

int main(){
    int num_input;
    cin >> num_input;
    int temp;
    for(int i = 0; i < num_input; i++){
        cin >> temp;
        cout << "Case #" << i+1 << ": ";
        countSheep(temp);
    }
    return 0;
}
