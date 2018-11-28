#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


int main(){
    freopen("/home/xiaodot/Downloads/B-large.in", "r", stdin);
    freopen("../out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int test=0; test<T; test++){
        int res = 0;
        string str;
        cin >> str;

        int len = str.length();
        int i = len;
        while(i>0){

            while(i > 0 && str[i-1] == '+') i--;

            if(i == 0) break;

            int cnt = 0;
            if(str[0] == '+') res++;
            while(str[cnt] == '+'){
                str[cnt] = '-';
                cnt++;
            }
            while(cnt<i && str[cnt]=='-') cnt++;

            reverse(str.begin(), str.begin() + i);
            for(int j=0; j<i; j++){
                str[j] = '+' + '-' - str[j];
            }
            res++;

            i -= cnt;
        }

        cout << "Case #" << test+1 << ": " << res << endl;
    }
    return 0;
}
