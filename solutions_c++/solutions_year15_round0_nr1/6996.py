#include <iostream>
#include <string>
#include <fstream>
#define S_MAX 1000
using namespace std;

int isDigit(char c){
    int i;
    if(c >= '0' && c <= '9'){
        i = c - '0';
        return i;
    }else{
        return -1;
    }
}

int cout_friend(int a[], int k){
    int sum = a[0];
    int sum_f = 0, n_f = 0;
    for(int i = 1; i <= k; i++){
        if(a[i] > 0){
            if(i > sum){
                n_f = i - sum;
                sum += n_f + a[i];
                sum_f += n_f;
            }else{
                sum += a[i];
            }
        }
    }
    return sum_f;
}

int main(void){
    int t;
    int max_k;
    ifstream fin;
    fin.open("A-large.in");
    fin >> t;
    for(int i = 0; i < t; i++){
        fin >> max_k;
        int a_k[S_MAX+1];
        char in;
        for(int j = 0; j <= max_k; j++){
            fin >> in;
            a_k[j] = isDigit(in);
        }
        int f_num = cout_friend(a_k, max_k);
        cout << "Case #" << i+1 << ": " << f_num << endl;
    }
    fin.close();
    return 0;
}
