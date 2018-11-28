#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;
bool isValid(long long val,int &map){

    while(val){
        map &= (~(1 << val % 10));
        val /= 10;
    }
    return map == 0;
}
int main(){
    long long n,val;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> val;
        cout << "Case #" << (i + 1) << ": ";
        //cout << val << endl;
        if(val == 0){
            cout << "INSOMNIA" << endl;
            continue;
        }
        int k = 1;
        int map = (1 << 10) - 1;
        do{

        }while(!isValid(val * (k++),map));
        cout << (val * (k-1)) << endl;
    }
    return 0;
}
