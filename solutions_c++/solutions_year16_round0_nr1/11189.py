#include<iostream>
#include<vector>

using namespace std;

void verifyDigits(long int x, vector<bool> & digits, int & count){//digits size is 10
    while(x){
        long int c = x%10;
        //cout << x << "\t" << c << endl;
        if(digits[c] == 0){
            digits[c] = 1;
            count++;
        }
        x /= 10;
    }
}//podria hacer qque retorne cuantos 1 hay en digits
int main(){
    long int t;
    cin >> t;
    for(long int i = 0; i < t; ++i){
        long int n;
        cin >> n;
        if(n){
            int count = 0;
            vector<bool> digits (10, 0);
            long int x = n;
            while(count != 10){
                verifyDigits(x, digits, count);
                //cout << count << endl;
                x+=n;
            }
            x-=n;
            cout << "Case #" << i+1 << ": " << x << endl;
        }
        else{
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
    }
    return 0;
}
