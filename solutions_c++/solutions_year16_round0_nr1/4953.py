#include<iostream>
using namespace std;
bool checkDigits(int digits[]){
    for(int i = 0; i < 10; i++)
        if(!digits[i])
            return false;
    return true;
}

int main(){
    long long int T, N, i, cases, number;
    cin>>T;
    cases = 1;
    while(cases <= T){
        cin>>N;
        if(N){
            int digits[10] = {0};
            for(i = 1; i < 1000000; i++){
                number = i * N;
                while(number){
                    digits[(number % 10)]++;
                    number /= 10;
                }
                if(checkDigits(digits)){
                    number = i * N;
                    break;
                }
            }
            cout<<"Case #"<<cases++<<": "<<number<<endl;
        }
        else
            cout<<"Case #"<<cases++<<": INSOMNIA"<<endl;
    }
    return 0;
}
