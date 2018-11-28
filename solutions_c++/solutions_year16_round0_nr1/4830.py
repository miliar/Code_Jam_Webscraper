#include <iostream>
#include <string>

using namespace std;

bool checkdigit(bool[]);

int main(){
    int T;
    cin >> T;
    int m = 1;
//    long long N = 0;
    while(m <= T){
        long long N;
        cin >> N;
        bool is1 = false;
        bool is2 = false;
        bool is3 = false;
        bool is4 = false;
        bool is5 = false;
        bool is6 = false;
        bool is7 = false;
        bool is8 = false;
        bool is9 = false;
        bool is0 = false;
        bool arr[10] = {is0, is1, is2, is3, is4, is5, is6, is7, is8, is9};
        long long k = 1;
        long long max = 0;
        if(N == 0){
            cout <<"Case #" << m <<": INSOMNIA"<<endl;
        }
        else{
            if( N <= 200){
                max = 1000000;
            }
            else{
                max = 10000000000000;
            }
            while(k < max){
                for(int i = 0; i < 10; i++){
                    long location = to_string(N*k).find(to_string(i));
                    if (location != -1){
                        arr[i] = true;
                    }
                }
                if (checkdigit(arr)){
                cout <<"Case #" << m <<": "<< k*N<<endl;
                break;
                }
                k++;
            }
            
            if(k == max){
            cout <<"Case #" << m <<": INSOMNIA"<<endl;
            }
        }
        m++;
//        N++;
    }
}

bool checkdigit(bool arr[]){
    bool ini = true;
    for(int j = 0; j < 10; j++){
        if(!(ini and arr[j])){
            return false;
        }
    }
    return true;
}
