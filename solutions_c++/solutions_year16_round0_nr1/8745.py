#include <iostream>
using namespace std;

struct ar{
    int value;
    bool used;
};

int main(){
    int test;
    long int N;
    ar num[10];
    int c=0;

    for(int k=0; k<10;k++){
        num[k].value = k;
    }

    cin >> test;

    for(int j = 1; j <= test; j++){

        for(int l=0; l<10;l++){
            num[l].used = false;
        }

        c = 0;
        cin >> N;
        long int steps = N;
        while(1){
            if(N == 0){
                break;
            }
            int temp = N;
            while(temp){
                int mod = temp %10;

                for(int i=0;i<10;i++){
                    if(num[i].value == mod && !(num[i].used)){
                        c++;
                        num[i].used = true;
                    }
                }
                temp /= 10;
            }

            if(c == 10){
                break;
            }
            N += steps;
        }

        if(steps){
          cout << "Case #"<<j<<": "<< N << endl;
        }else{
          cout << "Case #"<<j<<": "<<"INSOMNIA" <<endl;
        }
    }

    return 0;
}
