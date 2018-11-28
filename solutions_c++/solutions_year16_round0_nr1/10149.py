#include <iostream>

using namespace std;

void checkDigits(int array[], long long cnum);
int countSheep(long long cnum);

int main(){
    int n = 0;
    long long cnum = 0;
    long long result = 0;
    
    cin >> n;
    for(int i = 1; i < n+1; i++){
        cin >> cnum;
        result = countSheep(cnum);
        if(result == -1){
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
        else{
            cout << "Case #" << i << ": " << result << endl;
        }
    }
    
    return 0;
}

int countSheep(long long cnum){
    int array[10] = {0,0,0,0,0,0,0,0,0,0};
    int sum = 0;
    long count = 0;
    long testn = 0;
    if(cnum == 0){
        return -1;
    }
    while(true){
        for(int i = 0; i < 10; i++){
            sum += array[i];
            //cout << i << ": "<< array[i] << endl;
        }
        if(sum == 10){
            return testn;
        }
        testn = 0;
        sum = 0;
        count++;
        testn = cnum * count;
        //cout << "passing: " << testn << endl;
        checkDigits(array, testn);
    }
    return 0;
}

void checkDigits(int array[], long long cnum){
    int n = 0;
    if(cnum >= 10){
        n = cnum % 10;
        //cout << "n: "<< n << endl;
        if(array[n] != 1){
            array[n] = 1;
        }
        cnum /= 10;
        checkDigits(array, cnum);
    }
    else if(cnum > 0){
        n = cnum;
        if(array[n] != 1){
            array[n] = 1;
        }
    }
}