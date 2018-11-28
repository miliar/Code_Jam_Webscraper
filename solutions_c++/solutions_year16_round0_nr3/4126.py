#include <iostream>
#include <cmath>
using namespace std;

void nextJamcoin(int jamcoin[], int N){
    int i = 1, carry = 1, sum;
    while((i < N - 1) && carry){
    	sum = jamcoin[i] + carry;
        jamcoin[i] = sum % 2;
        carry = sum / 2;
        i++;
    }
}
int main(){
    long long int T, N, J, i, j, count = 0, value, temp, divisors[9];
    cin>>T>>N>>J;
    cout<<"Case #1: \n";
    int jamcoin[N];
    jamcoin[0] = jamcoin[N - 1] = 1;
    for(i = 1; i < N - 1; i++)
        jamcoin[i] = 0;
    do{
        for(i = 2; i < 11; i++){
            temp = 1;
            value = 0;
            for(j = 0; j < N; j++){
                value += jamcoin[j] * temp;
                temp *= i;
            }
            for(j = 2; j <= sqrt(value); j++)
                if(value % j == 0)
                    break;
            if(j > sqrt(value))
                break;
            divisors[i - 2] = j;
        }
        if(i == 11){
            for(j = N - 1; j >= 0; j--)
                cout<<jamcoin[j];
            for(j = 0; j < 9; j++)
                cout<<" "<<divisors[j];
            cout<<endl;
            count++;
        }
        nextJamcoin(jamcoin, N);
    }while(count < J);
    return 0;
}
