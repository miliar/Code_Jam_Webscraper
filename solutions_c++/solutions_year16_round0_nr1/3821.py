#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int sheepCount(int _N){
    if(_N <= 0)
        return -1;

    int total = 0;
    bool digits[10] = {false};
    int multiplyer = 1;
    do{

        int N = _N * multiplyer;
        while(N > 0){
            if(digits[N % 10] == false){
                digits[N % 10] = true;
                total++;
            }
            N /= 10;
        }
        if(total >= 10)
            break;
        multiplyer++;
    }
    while(total < 10);

    return _N * multiplyer;
}

int main(){

int num = 0;

cin>>num;

for(int i = 0 ; i < num ;++i){
    int N = 0;
    cin>>N;
    int ans = sheepCount(N);
    if( ans < 0)
        printf("Case #%d: INSOMNIA\n", i + 1);
    else
        printf("Case #%d: %d\n", i + 1, ans);
}

return 0;
}
