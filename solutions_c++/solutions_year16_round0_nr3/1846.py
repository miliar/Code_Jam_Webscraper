#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <random>
#include <functional>
using namespace std;

void use_file(const std::string& s = "")
{
    if (s != "std" && s != ""){
        freopen((s+".in").c_str(), "r", stdin);
        freopen((s+".out").c_str(), "w", stdout);
    }
}

int pow_mod(int x, int y, int mod)
{
    long long m = x;
    long long res = 1;
    while (y){
        if (y & 1){
            res *= m;
            res %= mod;
        }
        m *= m;
        m %= mod;
        y >>= 1;
    }
    return res % mod;
}


string to_bin_array(unsigned x, int N)
{
    string str = string(N, '0');
    for (int i = 0; i < N; i++){
        if ((x >> i) & 1){
            str[i] = '1';
        }
    }
    return str;
}


int judge(int base, const std::string& s)
{
    for (int mod = 2; mod <= 1000; mod++){
        int res = 0;
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '1'){
                res += pow_mod(base, i, mod);
            }
        }
        res %= mod;
        if (res == 0){
            return mod;
        }
    }
    return -1;
}

bool judge(const std::string& s, vector<int>& vec){
    for (int i = 0; i < 9; i++){
        int mod = judge(i + 2, s);
        if (mod == -1) return false;
        else vec[i] = mod;
    }
    return true;
}

void solve(int N, int J){
    std::default_random_engine generator;
    std::uniform_int_distribution<unsigned> rng(0, (1<<(N-2)) - 1);
    auto dice = std::bind(rng, generator);
    set<unsigned> st;

    std::vector<int> vec(9);
    while (J--){
        std::string bin;
        unsigned x;
        do {
            x = dice();
            x = (x << 1) | 1 | (1 << (N-1));
            bin = to_bin_array(x, N);
        }while(st.find(x) != st.end() || !judge(bin, vec));
        reverse(bin.begin(), bin.end());
        cout << bin;
        for (int i = 0; i < 9; i++){
            cout << " " << vec[i];
        }
        cout << endl;
    }
}

int main(){
    use_file("C2");
    cout << "Case #1:" << endl;
    solve(32, 500);
	return 0;
}
