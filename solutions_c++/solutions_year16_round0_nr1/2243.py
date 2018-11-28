//
//  pa.cpp
//  
//
//  Created by 宋元堯 on 2016/4/9.
//
//

#include <iostream>

using namespace std;

void digit(int i, bool *arr)
{
    while(i){
        arr[i % 10] = true;
        i /= 10;
    }
}

bool check(bool *arr)
{
    bool res = true;
    for(int i = 0; i < 10; ++i){
        res = res & arr[i];
    }
    return res;
}

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i){
        bool arr[10] = {false};
        int N;
        cin >> N;
        if(!N){
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        int a = 0;
        while(true){
            a += N;
            digit(a, arr);
            if(check(arr)) break;
        }
        cout << "Case #" << i << ": " << a << endl;
    }
    return 0;
}
