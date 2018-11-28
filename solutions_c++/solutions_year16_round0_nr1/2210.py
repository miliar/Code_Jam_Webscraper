#include <iostream>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

void use_file(const std::string& s = "")
{
    if (s != "std" && s != ""){
        freopen((s+".in").c_str(), "r", stdin);
        freopen((s+".out").c_str(), "w", stdout);
    }
}

int calc_digits(std::set<int>& st, long long s)
{
    while (s){
        st.insert(s % 10);
        s /= 10;
    }
    return st.size();
}

long long solve(long long x)
{
    if (x == 0){
       return -1;
    }
    std::set<int> st;
    long long ori = x;
    while (calc_digits(st, x) < 10){
        x += ori;
    }
    return x;
}

void test()
{
    for (int i = 1; i <= 1000000; i++){
        std::cout << i << " " << solve(i) << std::endl;
    }
}

int main()
{
    use_file("A2");
    int N, x;
    cin >> N;
    for (int ca = 1; ca <= N; ca++){
        cin >> x;
        long long s = solve(x);
        std::cout << "Case #" << ca << ": ";
        if (s == -1) std::cout << "INSOMNIA" << std::endl;
        else std::cout << s << std::endl;
    }
    return 0;
}
