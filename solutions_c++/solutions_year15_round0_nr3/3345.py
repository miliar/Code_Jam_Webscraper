#include <iostream>
#include <map>

using namespace std;

char LString[10000];

struct Result {
    char mag;
    int sign;
    bool operator==(const Result &that) {
        return this->sign == that.sign && this->mag == that.mag;
    }
    bool operator!=(const Result &that) {
        return !(*this==that);
    }
};

map<char, map<char, Result> > mult;
Result R1 = {'1', 1};
Result R2 = {'1', -1};
Result R3 = {'i', 1};
Result R4 = {'i', -1};
Result R5 = {'j', 1};
Result R6 = {'j', -1};
Result R7 = {'k', 1};
Result R8 = {'k', -1};

Result multiply(Result a, Result b) {
    Result result;
    result = mult[a.mag][b.mag];
    result.sign *= a.sign*b.sign;
    return result;
}

int main() {
    mult['1'] = {{'1', R1}, {'i', R3}, {'j', R5}, {'k', R7}};
    mult['i'] = {{'1', R3}, {'i', R2}, {'j', R7}, {'k', R6}};     
    mult['j'] = {{'1', R5}, {'i', R8}, {'j', R2}, {'k', R3}};     
    mult['k'] = {{'1', R7}, {'i', R5}, {'j', R4}, {'k', R2}};     
    int t, L, X;
    cin>>t;
    int iter = 1;
    std:string ans;
    while(t-- != 0) {
        ans = "NO";
        cin>>L;
        cin>>X;
        for (int i = 0; i < L; i++) {
            cin>>LString[i];
        }
        Result r = R1;
        Result r_rev = R1;
        int i_pos = -1;
        int k_pos = -1;
        for (int i = 0; i < L*X; i++) {
            r = multiply(r, {LString[i%L], 1});
            r_rev = multiply({LString[(L*X - i -1)%L], 1}, r_rev);
            if (i_pos == -1 && r == R3) {
                i_pos = i;
            }
            if (k_pos == -1 && r_rev == R7) {
                k_pos = L*X - i - 1;
            }
        }
        if (r == R2 && i_pos != -1 && k_pos != -1 && k_pos - i_pos > 1) {
            ans = "YES";
            //Result t = R1;
            //for (int i = i_pos + 1; i < k_pos; i++) {
            //    t = multiply(t, {LString[i%L], 1});
            //} 
            //if (t != R5) {
            //    cout<<"Something wrong"<<endl;
            //}
        }
        cout<<"Case #"<<iter<<": "<<ans<<endl;
        iter++;
    }
    return 0;
}
