#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

bool complete(bool array[], long long int n){
    for(long long int i = 0;i < n;i++){
        if(array[i] == false){
            return false;
        }
    }
    return true;
}

void digits(bool array[], long long int n){
    while(n != 0){
        long long int temp = n % 10;
        n /= 10;
        array[temp] = true;
    }
}

int main(){
    long long int t, n;
    cin >> t;
    bool array[10];
    long long int counter = 1;
    while(t--){
        memset(array, false, sizeof(array));
        cin >> n;
        if(n == 0){
            cout << "Case #" << counter << ": " << "INSOMNIA" << endl;
            counter++;
            continue;
        }
        long long int count = 1;
        long long int move = n;
        while(!complete(array, 10)){
            digits(array, move);
            count++;
            move = n*count;
        }
        cout << "Case #" << counter << ": " << move - n << endl;
        counter++;
    }
    return 0;
}
