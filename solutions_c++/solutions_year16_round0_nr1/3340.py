#include <bits/stdc++.h>
using i64 = long long;
using u64 = unsigned long long;
using u32 = unsigned;
using namespace std;
bool check(bool* arr){
    for (int i = 0; i < 10; ++i) {
        if (!arr[i])
            return false;
    }
    return true;
}
int main() {
    ios::sync_with_stdio(false);
    u64 N;
    ifstream input("in.txt");
    ofstream output("out.txt");
    input >> N;
    for(size_t i = 0; i < N; ++i){
        bool digits[10];
        memset(digits, 0, 10);
        u64 S;
        input >> S;
        u64 cnt = 1;
        u64 Num;
        while(!check(digits) && cnt <= 60){
            Num = cnt++ * S;
            u64 P = Num;
            while(P > 0){
                digits[P % 10] = true;
                P /= 10;
            }
        }
        output << "Case #" << i + 1 << ": ";
        if (check(digits))
             output << Num << "\n";
        else
            output << "INSOMNIA\n";
    }
    return 0;
}