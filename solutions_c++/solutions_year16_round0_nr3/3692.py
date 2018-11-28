#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>

using namespace std;

long long N, K;

long long to_decimal(string n, int b){
    int x = 0;
    long long decimal = 0;
    for(int i = n.size()-1; i >= 0; i--){
        decimal += (n[i]-48) * pow(b, x);
        x++;
    }
    return decimal;
}

long long getDivisor(long long n){
    for(long long i = 2; i < sqrt(n); i++){
        if(n%i == 0) return i;
    }
    return 0;
}

string to_binary(int n){
    bitset<32> b1(n);
    string bits = b1.to_string();
    int pos;
    if((pos = bits.find('1')) != string::npos){
        return bits.substr(pos);
    }
    return b1.to_string();
}

int main(){
    int TC;
    cin >> TC;
    for(int c = 1; c <= TC; c++){
        cin >> N >> K;
        vector<long long> temp;
        printf("Case #%d:\n", c);
        for(int i = 1ULL << N-1; i < (1ULL << N) && K; i++){
            string binaryValue = to_binary(i);
            temp.clear();
            if(i%2 == 1){
                for(int b = 2; b <= 10; b++){
                    long long newBase = to_decimal(binaryValue, b);
                    long long x = getDivisor(newBase);
                    if(x){
                        temp.push_back(x);
                    }
                }
                if(temp.size() == 9){
                    cout << binaryValue << " ";
                    for(int i = 0; i < 9; i++)printf("%lld%s", temp[i], i < 8 ? " ":"");
                    printf("\n");
                    K --;
                }
            }
        }
    }
    return 0;
}
