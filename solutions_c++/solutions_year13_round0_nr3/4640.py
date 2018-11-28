#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <stdio.h>
using namespace std;
int reverseint(int num)
{
        int inv = 0;
        while (num>0){
                inv = inv*10 + (num%10);
                num = num/10;
        }
        return inv;
}

int main(){
    int T;
    int A;
    int B;
    int count;
    vector<int> fair;
    cin >> T;
    for(int i = 0; i< T; i++){
        cin >> A;
        cin >> B;
        count = 0;
        for(int j = A; j <= B; j++){
            if(j == reverseint(j) && sqrt(j) == (int)sqrt(j) && reverseint((int)sqrt(j)) == sqrt(j) ){
                count++;
            }

        }
        cout << "Case #" << i+1 << ": " << count << endl;

    }

}
