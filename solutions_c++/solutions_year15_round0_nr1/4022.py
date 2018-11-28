#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdio>

using namespace std;


int main(){
    freopen("./input.txt", "r", stdin);
    freopen("./output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int test=1; test<=T; test++){

        int res = 0, sum = 0, sz;
        scanf("%d", &sz);
        getchar();

        for(int i=0; i<=sz; i++){
            int num = getchar()-'0';
            if(sum < i){
                res += i-sum;
                sum = i;
            }
            sum += num;
        }
        cout << "Case #" << test << ": " << res;
        if(test < T) cout << endl;

    }
    return 0;
}
