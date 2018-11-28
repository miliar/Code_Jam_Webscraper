#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

typedef unsigned long long ULL;

string gen(ULL num ,int len){
    string ans(len, '0');
    int i = len - 1;
    while(num > 0){
        if(num % 2 == 1) ans[i] = '1';
        num /= 2; i--;
    }
    return ans;
}

ULL convert(string s, int b){
    int n = 0;
    ULL ans = 0;
    for(int i = s.size()-1; i>=0 ; i--){
        if(s[i] == '1')
            ans += pow(b, n);
        n++;
    }
    return ans;
}

int main(){
    int NN;
    cin >> NN;
    for(int nn = 1; nn <= NN; nn++){
        cout << "Case #" << nn << ": " << endl;
        int N, J;
        cin >> N >> J;
        ULL genNum = pow(2, N) - 1;
        /*
        for(int base = 2; base <= 10; base++){
            //cout << convert("100011", base) << endl;
        }*/
        int succ = 0;
        for(int num = genNum /2 - 1; num <= genNum; num++){
            string str = gen(num, N);
            if(str[0] == '0' or str[str.size()-1] == '0') continue;
            vector<ULL> divisor;
            bool cont = true;
            for(int base = 2; base <= 10; base++){
                ULL numb = convert(str, base);
                for(ULL d = 2; d <= 1 + sqrt(numb); d++ ){
                    if(numb % d == 0){
                        divisor.push_back(d);
                        break;
                    }
                }
                //cout << convert("100011", base) << endl;
            }
            if(divisor.size() == 9){
                succ++;
                cout << str << ' ';
                for(auto v: divisor)
                    cout << v << ' ';
                cout << endl;
            }
            if(succ == J)
                break;
        }
    }
    return 0;
}