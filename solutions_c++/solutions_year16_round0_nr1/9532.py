#include<stdio.h>
#include<string>
#include<iostream>
#include<string.h>

using namespace std;

int main(){
    int T, vet[10], flag;
    long long int N, f;
    string str;
    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> N;
        long long int aux = N;
        flag = 0;

        if(N == 0){
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
            continue;
        }

        memset(vet, 0, 10*sizeof(int));
        int k = 1;

        while(flag != 1){
            flag = 1;
            f = N;
            while(N > 0){
              vet[N % 10] = 1;
              N = N / 10;
            }
            for(int j = 0; j < 10; j++){
                if(vet[j] == 0){
                    flag = 0;
                    break;
                }
            }

            N = aux * ++k;
        }
        cout << "Case #" << i+1 << ": " << f <<  endl;
    }
}
