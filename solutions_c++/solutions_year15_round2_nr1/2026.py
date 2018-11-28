#include "common.hpp"
using namespace std;


static vector<ullong> dpr;
static vector<ullong> dp;
static map<ullong,ullong> memo;


ullong reverse(ullong n) {
    stringstream buffer1;
    buffer1 << n;
    string digits(buffer1.str());
    reverse(begin(digits), end(digits));

    stringstream buffer(digits);
    ullong reversed;
    buffer >> reversed;
    return reversed;
}

ullong compute(ullong n) {
    if(0 == n)
        return 0;

    cerr << "compute(" << n << ")" << endl;

    if(end(memo) != memo.find(n)) {
        auto v = memo[n];
        cerr << "memo[" << n << "] = " << v << "*" << endl;
        return v;
    }

    memo[n] = n;
    auto v = compute(n-1)+1;
    auto r = reverse(n);
    //if(reverse(r) == n && r != n)
        v = min(v, compute(r)+1);
    cerr << "memo[" << n << "] = " << v << endl;
    memo[n] = v;
    return v;
}

void setup_dp()
{
    if(dp.size())
        return;

    ullong Nmax = 10000001ul;
    //ullong Nmax = 101ull;
    dp.resize(Nmax);
    dpr.resize(Nmax);
    iota(begin(dp), end(dp), 0ull);
    for(ullong n=0; n<dp.size(); ++n) {
        dpr[n] = reverse(n);
    }

    bool changed = true;
    while(changed) {
        changed = false;
        for(ullong n=3; n<Nmax; ++n) {
            auto r = dpr[n];
            if((dp[r] > dp[n]+1)) {
                changed = true;
                dp[r] = dp[n]+1;
            }
            if(dp[n] > dp[n-1]+1) {
                changed = true;
                dp[n] = dp[n-1]+1;
            }
        }
    }

    //for(ullong n=0; n<dp.size(); ++n) {
    //    cerr << "dp[" << n << "] = " << dp[n] << endl;
    //}
}

void codejam::solve_small(int testno, std::istream& in, std::ostream& out)
{
    ullong N;
    in >> N;

    setup_dp();

    //cerr << testcase(testno) << " N = " << N << endl;
    //auto v = compute(N); // dp[N]

    auto v = dp[N];
    out << testcase(testno) << v << endl;
}

void codejam::solve_large(int testno, std::istream& in, std::ostream& out)
{
    solve_small(testno, in, out);
}

int main(int argc, char* argv[]) {
    codejam cj("A");
    return cj.run(argc, argv);
}
